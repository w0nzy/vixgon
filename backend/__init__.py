import jwt
import base64
import secrets
from typing import Annotated
from fastapi import (
    FastAPI,
    Depends
    )
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from argon2 import PasswordHasher
from backend.db import Database, DatabaseRegisterCode, DatabaseUserRegisterModel
from backend.models import UserDataModel, UserLoginDataModel, UserRegistrationResponseModel
from backend.models import LoginModel
from backend.util import read_user_photo
from modules.vixgon_log import create_logger
from backend.hash import compare_hash
logger = create_logger()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/vixgon/api/login")
backend_api = FastAPI()
argon2 = PasswordHasher()
database = Database("main.db")
database.init_db()
jwt_secret_key = "0b1211543e2971991cc26974b53e7a5b9adf00576d8d82c9de38e691b1b3110e"
def verify_hash(pwd_hash: str,pwd: str) -> bool:
    try:
        argon2.verify(pwd_hash,pwd)
    except:
        return False
    return True

def validate_user_token(token_data: Annotated[str,Depends(oauth2_scheme)]):
    try:
        decoded_jwt = jwt.decode(token_data,jwt_secret_key,algorithms=["HS256"])
        username = decoded_jwt.get("sub")
    except:
        raise HTTPException(status_code = 401,detail = "Expired token",headers = {"WWW-Authenticate":"Bearer"})

@backend_api.post("/vixgon/api/login")
def login(data: LoginModel) -> UserLoginDataModel:
    if verify_hash("$argon2id$v=19$m=65536,t=3,p=4$8BkqIYg020xAxnYB9oKN0Q$omVaEx1bvfVTB4llRH3q1eF3YKkV7reh1iywPs6WRYw",data.password):
        return UserLoginDataModel(auth_token = secrets.token_hex(32),user_photo = base64.b64encode(secrets.token_bytes(32)).decode())
    raise HTTPException(status_code = 401,detail = "Bad username or password")

@backend_api.post("/vixgon/api/register")
async def register_user(data: UserDataModel) -> UserRegistrationResponseModel:
    result = database.push_user(user_data = DatabaseUserRegisterModel(
        username = data.username,
        password = data.password,
        name = data.name,
        surname = data.surname,
        age = data.age,
        user_type = data.user_type,
        gender = data.gender,
        registertration_time = data.registertration_time,
        user_photo_name  = data.user_photo_data
        ))
    match result:
        case DatabaseRegisterCode.USER_ALREADY_EXISTS:
            return UserRegistrationResponseModel(detail = "User already exists")
        case DatabaseRegisterCode.USER_CREATED_SUCCESSFULLY:
            return UserRegistrationResponseModel(detail = "User created successfully")
        case DatabaseRegisterCode.BAD_PARAMETER_LIST:
            return UserRegistrationResponseModel(detail = "Check username or password contains bad value")
        case _:
            return UserRegistrationResponseModel(detail = "Unknown error %s" % (result))
            logger.critical("Cannot register user :( )")
@backend_api.post("/vixgon/test")
async def test_data() -> dict:
    return {"token":secrets.token_hex(32)}
@backend_api.get("/vixgon/api/get_users")
async def get_users() -> dict:
    return {"users":database.extract_all_users()}
@backend_api.get("/vixgon/api/get_user/{user_name}")
async def get_user(user_name: str) -> UserDataModel:
    return database.extract_user(user_name)
@backend_api.post("/vixgon/login_test")
async def login_test(user_input: LoginModel) -> UserLoginDataModel:
    if database.get_username_count(user_input.username) != 0 and (user_data := database.extract_user(user_input.username)):
        if compare_hash(user_input.password,user_data.password):
            logger.info("User %s logged in" % (user_input.username))
            return UserLoginDataModel(user_name = user_data.username,user_surname = user_data.surname,user_photo = read_user_photo(user_data.username),auth_token = secrets.token_hex(16))
    logger.warning("Wrong password or username %s:%s" % (user_input.username,user_input.password))
    return UserLoginDataModel(auth_token="no_token",user_name="no_username",user_surname="no_surname",user_photo="no_photo")