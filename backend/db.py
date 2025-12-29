import os
import sys
import sqlite3
sys.path.append(os.path.dirname(__file__))
from argon2 import PasswordHasher

from backend.enums import UserType
from modules.vixgon_log import create_logger
from backend.hash import hash_pwd
logger = create_logger()
argon2 = PasswordHasher()

class Database:
    def __init__(self,db_path: str):
        self.db_fname = db_path
        self.db_dir = os.path.join(os.path.dirname(__file__),"database")
        os.makedirs(self.db_dir,exist_ok=True)
        self.db_path = os.path.join(self.db_dir,self.db_fname)
        self.database = sqlite3.connect(self.db_path)
        self.cursor = self.database.cursor()
        self.opt = False
    def push_user(self,*,
                  username = "_not_set",
                  password = "_not_set",
                  name = "_set",
                  surname = "_set",
                  gender = "_notset",
                  user_type = 0,
                  age = 0,
                  registration_time = 0,
                  photo_data = "_not_set"
                  ):
        if username != "_not_set" and name != "_set" and surname != "_set" and gender != "_notset" and not age < 20 and user_type in [UserType.USER_TYPE_ADMIN,UserType.USER_TYPE_GUEST,UserType.USER_TYPE_WORKER] and registration_time != 0 and photo_data != "_not_set" and password != "_not_set" and self.opt:
            if (self.get_username_count(username) == 0):
                sql_command = "INSERT INTO users (username,password,name,surname,gender,age,user_type,registration_time) VALUES(?,?,?,?,?,?,?,?)"
                pwd = hash_pwd(password)
                if pwd != "":
                    self.cursor.execute(sql_command,(username,name,surname,pwd,gender,age,user_type,registration_time))
                    self.database.commit()
                    logger.info("User created %s" % (username))
                    return
                else:
                    print("Bad hash value")
            else:
                logger.error("User already exists %s" % (username))
        else:
            print("Bad parameter list :/ or not initalized database")
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
        if self.get_username_count(username) > 0:
            try:
                user_credentials = self.cursor.execute("SELECT * FROM users WHERE username = ?;",(username,)).fetchall()
                return user_credentials[0]
            except Exception as error:
                logger.critical("Cannot get data %s : %s" % (username,str(error)))
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