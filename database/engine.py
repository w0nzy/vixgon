
from typing import List
from sqlalchemy import create_engine, schema
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session
from sqlalchemy.orm import declarative_base

from database.models import Shelves,UserDatabaseModel
from database.models import check_tables
from database.return_models import ShelfDataModel
from modules.error_handling import error
from . import check_db_initialized_or_not
from .exceptions import ShelfAlreadyExistsException, UserAlreadyExistsException
from modules.vixgon_log import create_logger 

logger = create_logger()


class PostgreSQLDB:
    def __init__(self,
                 host: str = "127.0.0.1",port: int = 5432,
                 username: str = "postgres",
                 password: str = "alperen",
                 database: str = "vixgon"
                 ):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
    @error(return_value = False)
    def init(self) -> bool:
        logger.info("Database initialized :=)")
        self.engine = create_engine(f"postgresql+psycopg://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}")
        self.session = sessionmaker(bind = self.engine)
        check_tables(self.engine)
        return True
    @check_db_initialized_or_not
    @error(return_value = Session)
    def get_session(self) -> Session:
        return self.session()
    @check_db_initialized_or_not
    @error(return_value = ShelfDataModel)
    def get_shelf_data(self,shelf_name: str = "ABCDEF") -> ShelfDataModel:
        if (self.get_session()) is False:
            raise
        session = self.get_session()
        return ShelfDataModel(shelf_name = session.query(Shelves).filter(Shelves.shelf == shelf_name).first().shelf)
    @check_db_initialized_or_not
    @error(return_value = 0)
    def get_shelf_count(self,shelf_name: str) -> int:
        with self.get_session().begin():
            session = self.get_session()
            return session.query(Shelves).filter(Shelves.shelf == shelf_name).count()
    @check_db_initialized_or_not
    @error(return_value = 0)
    def get_username_count(self,username: str) -> int:
        session = self.get_session()
        return session.query(UserDatabaseModel).filter(UserDatabaseModel.username == username).count()
    @check_db_initialized_or_not
    @error(return_value=[ShelfDataModel])
    def get_shelves(self) -> List[ShelfDataModel]:
        return [ShelfDataModel(shelf_name = db_obj.shelf) for db_obj in self.get_session().query(Shelves).all()]
    @check_db_initialized_or_not
    @error(return_value = False)
    def push_shelf(self,*,shelf_name: ShelfDataModel) -> bool:
        if self.get_shelf_count(shelf_name) != 0:
            raise ShelfAlreadyExistsException("Shelf already exists :/ %s" % (shelf_name))
        session = self.get_session()
        session.add(Shelves(shelf = shelf_name))
        session.commit()
        return True
    @check_db_initialized_or_not
    @error(return_value = False)
    def push_user(self,*,
                  username: str,
                  password: str,
                  name: str,
                  surname: str,
                  gender: str,
                  age: int,
                  user_type: int,
                  registration_time: float,
                  user_photo_path: str) -> bool:
        if self.get_username_count(username) != 0:
            raise UserAlreadyExistsException("User %s exists" % (username))
        session = self.get_session()
        session.add(UserDatabaseModel( # add user_photo_path db and structure :7
            username = username,
            password = password,
            name = name,
            surname = surname,
            gender = gender,
            age = age,
            user_type = user_type,
            registration_time = registration_time,
            user_photo_path = user_photo_path
            ))
        session.commit()
        return True
    @check_db_initialized_or_not
    @error(return_value=False)
    def push_session(self,session: str):
        session_of_len = len(session)

    def __repr__(self):
        return "<%s username = %s host = %s port = %d database = %s>" % (self.__class__.__name__,self.username,self.host,self.port,self.database)