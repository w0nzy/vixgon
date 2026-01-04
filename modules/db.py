import os
import shutil
import base64
import sqlite3
from requests import auth
from .enums import DatabaseRegisterCode

from .vixgon_log import create_logger
from .db_models import LocalCredentialsModel

from . import get_app_path, get_local_database_path
from . import get_user_photo_path
from . import create_uuid
from . import can_decodeb64data

logger = create_logger()
class ClientDatabase:
    def __init__(self,*,database: str = get_local_database_path()):
        self.database_file = database
        self.database = None
        self.cursor = None
    def init_db(self):
        if self.check_db_initialized_or_not():
            try:
                logger.info("Database initialized :)")
                self.database = sqlite3.connect(self.database_file)
                self.cursor = self.database.cursor()
                self.cursor.execute("""CREATE TABLE IF NOT EXISTS login_credentials (
                username VARCHAR(25) NOT NULL,
                user_token VARCHAR(32) NOT NULL,
                user_photo_path VARCHAR(255) NOT NULL
                )""")
                self.database.commit()
            except Exception as sql_init_error:
                logger.critical("Cannot initialize local database :/ %s" % (str(sql_init_error)))
    def push_user_login_credentials(self,*,user_data: LocalCredentialsModel = LocalCredentialsModel()):
        username_len = len(user_data.username)
        auth_token_len = len(user_data.token)
        if self.check_db_initialized_or_not():
            logger.warning("Not initialized database :/")
            return False
        if (
            (0 < username_len <= 25) and 
            (0 < auth_token_len <= 32)
            ):
            try:
                user_photo_path = os.path.join(get_user_photo_path(create_uuid()))
                self.cursor.execute("INSERT INTO login_credentials (username,user_token,user_photo_path) VALUES(?,?,?);",(user_data.username,user_data.token,user_photo_path))
                logger.info("New local user created %s:%s" % (user_data.username,user_data.token))
                self.database.commit()
                return self.save_photo(user_photo_path,user_data.user_photo)
            except Exception as sql_error:
                logger.critical("Cannot create user %s sql error is %s" % (user_data.username,str(sql_error)))
                return False
        logger.critical("Cannot create user username: %s len(%s) token: %s len(%s) is_validb64data: %s" % (user_data.username,username_len,user_data.token,auth_token_len,can_decodeb64data(user_data.user_photo)))
        return False
    def extract_user_credentials(self) -> LocalCredentialsModel:
        return_model = LocalCredentialsModel()
        if self.check_db_initialized_or_not():
            logger.warning("Database is not initialized")
        try:
            data = self.cursor.execute("SELECT * FROM login_credentials;").fetchall()[0]
            return_model.username = data[0]
            return_model.token = data[1]
            return_model.user_photo_path = data[2]
        except Exception as sql_fetch_error:
            logger.critical("Cannot fetch data :/ %s " % (str(sql_fetch_error)))
        return return_model
    def check_db_initialized_or_not(self) -> bool:
        """
        WARNING: it's returns true if database is not initialized
        """
        return self.cursor is None and self.database is None
    def save_photo(self,path: str,content: bytes) -> bool:
        logger.info("Saving user photo :) %s " % (path))
        if can_decodeb64data(content):
            logger.info("Data is can decodable format type %s" % (content.__class__.__name__))
            content = base64.b64decode(content) #
        content = content
        try:
            with open(path,"wb") as fd:
                fd.write(content)
        except Exception as err:
            logger.critical("Cannot save user photo %s " % (str(err)))
            return False
        return True
    def get_photo_data(self,photo_name: str) -> bytes:
        photo_path = get_user_photo_path(photo_name)
        if not os.path.exists(photo_path):
            logger.critical("%s file doesnt exists" % (photo_path))
            return b""
        try:
            with open(photo_path,"rb") as fd:
                return fd.read()
        except Exception as read_error:
            logger.critical("Cannot read file %s: %s" % (photo_path,str(read_error)))
        return b""
    def close(self):
        logger.info("Database is closing")
        if not self.check_db_initialized_or_not():
            try:
                self.database.close()
                self.cursor = None
                self.database = None
                logger.info("Database is closed ")
            except Exception as sql_error:
                logger.critical("Cannot close db %s " % (str(sql_error)))
            return
        logger.info("Database cannot close because it's not opened anyway")