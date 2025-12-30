import os
import sys
import sqlite3
sys.path.append(os.path.dirname(__file__))

from argon2 import PasswordHasher
from backend.enums import UserType
from backend.enums import DatabaseRegisterCode
from modules.vixgon_log import create_logger
from backend.hash import hash_pwd
from backend.models import DatabaseUserRegisterModel

logger = create_logger()
argon2 = PasswordHasher()

class Database:
    def __init__(self,db_path: str):
        self.db_fname = db_path
        self.db_dir = os.path.join(os.path.dirname(__file__),"database")
        os.makedirs(self.db_dir,exist_ok=True)
        self.db_path = os.path.join(self.db_dir,self.db_fname)
        self.database = sqlite3.connect(self.db_path,check_same_thread = False)
        self.cursor = self.database.cursor()
        self.opt = False
    def push_user(self,*, # fix here :/ too bad
                  user_data: DatabaseUserRegisterModel = None
                  ) -> DatabaseRegisterCode:
        if not self.opt:
            logger.warning("Database is not initialized cannot register user %s" % (user_data.username))
            return DatabaseRegisterCode.NOT_INITIALIZED_DATABASE
        if not self.check_user_registration_input(user_data):
            logger.warning("Bad parameter list %s" % (user_data))
            return DatabaseRegisterCode.BAD_PARAMETER_LIST
        if self.get_username_count(user_data.username) != 0:
            logger.warning("User already exists %s" % (user_data.username))
            return DatabaseRegisterCode.USER_ALREADY_EXISTS
        pwd = hash_pwd(user_data.password)
        if pwd == "":
            return DatabaseRegisterCode.BAD_HASH_VALUE
        user_data.password = pwd
        sql_command = "INSERT INTO users (username,password,name,surname,gender,age,user_type,registration_time) VALUES(?,?,?,?,?,?,?,?)"
        try:
            self.cursor.execute(sql_command,tuple(list(user_data.__dict__.values())[:-1]))
            self.database.commit()
            logger.info("User created %s" % (user_data.username))
        except Exception as user_registration_error:
            logger.critical("Cannot register user %s because %s error occured" % (user_data.username,str(user_registration_error)))
            return DatabaseRegisterCode.SQL_ERROR
        return DatabaseRegisterCode.USER_CREATED_SUCCESSFULLY
    def push_shelf(self,shelf): pass
    def init_db(self):
        try:
            self.database.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username VARCHAR(25) NOT NULL,
                    password VARCHAR(32) NOT NULL,
                    name VARCHAR(25) NOT NULL,
                    surname VARCHAR(25) NOT NULL,
                    gender VARCHAR(25) NOT NULL,
                    age INTEGER NOT NULL,
                    user_type INTEGER,
                    registration_time INTEGER
                )
                """)

            self.database.execute("""
            CREATE TABLE IF NOT EXISTS shelves (
                shelf VARCHAR(10) NOT NULL,
                created_by VARCHAR(25) NOT NULL,
                creation_time INTEGER,
                id INTEGER PRIMARY KEY AUTOINCREMENT
            )
            """)

            self.database.execute("""
            CREATE TABLE IF NOT EXISTS item_logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT
            )
            """)
            self.database.commit()
            self.opt = True
            logger.info("Database initialized")
        except Exception as db_error:
            logger.critical("Cannot initialized data ")
            print("Cannot initialize db ",db_error)
    def get_username_count(self,username: str):
        result = 0
        try:
            result = self.cursor.execute("SELECT COUNT(*) FROM users WHERE username = ?;",(username,)).fetchone()[0]
            logger.info("Username %s count is %s" % (username,result))
        except Exception as fetch_error:
            logger.critical("Cannot get %s count error %s" % (username,fetch_error))
        return result
    def close(self):
        if self.opt:
            try:
                logger.info("Closing database")
                self.database.close()
                self.opt = False
            except Exception as db_error:
                logger.critical("cannot close close %s" % (str(db_error)))
                print("Cannot close db ",db_error)
    def extract_user(self,username: str):
        user_credentials = []
        if self.get_username_count(username) > 0:
            try:
                user_credentials = self.cursor.execute("SELECT * FROM users WHERE username = ?;",(username,)).fetchone()
            except Exception as error:
                logger.critical("Cannot get data %s : %s" % (username,str(error)))
        return user_credentials
    def extract_user_pwd(self,username: str) -> str:
        if self.get_username_count(username) == 0:
            return ""
        pwd = ""
        try:
            pwd = self.cursor.execute("SELECT password FROM users WHERE username = ?;",(username,)).fetchone()
        except Exception as pwd_fetch_error:
            logger.critical("Cannot fetch user pwd !",pwd_fetch_error)
            return pwd
        return pwd

    def extract_all_users(self) -> list:
        users = []
        try:
            users = self.cursor.execute("SELECT * FROM users;").fetchall()
        except Exception as sql_error:
            logger.critical("Cannot get users error %s" % (str(sql_error)))
        return users
    @classmethod
    def check_user_registration_input(cls,input: DatabaseUserRegisterModel) -> bool:
        if not isinstance(input,DatabaseUserRegisterModel):
            return False # anormal data type
        model_members = DatabaseUserRegisterModel().__dict__
        return all([getattr(input,member) != model_members[member] for member in model_members.keys()])
        