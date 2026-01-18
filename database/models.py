from sqlalchemy.orm import declarative_base
from sqlalchemy import (
    Column,Integer,
    String,REAL,inspect
)

BaseModel = declarative_base()
class UserDatabaseModel(BaseModel):
    __tablename__ = "userinfo"
    user_id = Column(Integer,autoincrement = True,primary_key = True)
    username = Column(String(25),nullable = False,unique=True)
    password = Column(String(25),nullable = False)
    name = Column(String(25),nullable = False)
    surname = Column(String(25),nullable = False)
    gender = Column(String(25),nullable = False)
    age = Column(Integer,nullable = False)
    user_type = Column(Integer,nullable = False)
    registration_time = Column(REAL,nullable = False)
    user_photo_path = Column(String(255),nullable = False) # 255 => win32 MAX_PATH

class Shelves(BaseModel):
    __tablename__ = "shelves"
    shelf_id = Column(Integer,autoincrement = True,primary_key = True)
    shelf = Column(String(10),nullable = False,unique=True,default = "no_shelf")
class Sessions(BaseModel):
    __tablename__ = "sessions"
    session_id = Column(Integer,autoincrement = True,primary_key = True)
    session = Column(String(200),unique = True)

def check_tables(engine):
    BaseModel.metadata.create_all(checkfirst = True,bind = engine)
