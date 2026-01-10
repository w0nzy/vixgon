import jwt
import base64
import secrets
from typing import Annotated
from datetime import timedelta
from datetime import datetime
from datetime import timezone

from fastapi import (
    FastAPI,
    Depends
    )
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from argon2 import PasswordHasher
from pydantic import Secret
from backend.db import Database, DatabaseRegisterCode, DatabaseUserRegisterModel
from backend.models import UserDataModel, UserLoginDataModel, UserRegistrationResponseModel
from backend.models import LoginModel
from backend.util import read_user_photo
from modules.vixgon_log import create_logger
from backend.hash import compare_hash
logger = create_logger()
backend_api = FastAPI()
argon2 = PasswordHasher()
database = Database("main.db")
database.init_db()
jwt_secret_key = "0b1211543e2971991cc26974b53e7a5b9adf00576d8d82c9de38e691b1b3110e"

def validate_user_token(token_data):
    try:
        decoded_jwt = jwt.decode(token_data,jwt_secret_key,algorithms=["HS256"])
        username = decoded_jwt.get("sub")
    except Exception as e:
        logger.critical("Validation error %s" % (str(e)))
        raise HTTPException(status_code = 401,detail = "Expired token",headers = {"WWW-Authenticate":"Bearer"})
    return token_data
def create_token(payload: dict,remember_me = False) -> str:
    payload = payload.copy()
    payload.update({"exp":datetime.now(timezone.utc) + timedelta(minutes =1)})
    try:
        data = jwt.encode(payload,jwt_secret_key,algorithm="HS256")
    except jwt.PyJWTError as jwt_error:
        logger.critical("Cannot encode jwt %s:/" % (str(jwt_error)))
        return ""
    logger.info("Token created %s " % (data))
    return data
@backend_api.post("/vixgon/api/login")
def login(data: LoginModel) -> UserLoginDataModel:
    pass

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

@backend_api.post("/vixgon/api/login_test")
async def login_test(user_input: LoginModel) -> UserLoginDataModel:
    print("User input ",user_input)
    if database.get_username_count(user_input.username) != 0 and (user_data := database.extract_user(user_input.username)):
        if compare_hash(user_input.password,user_data.password):
            logger.info("User %s logged in" % (user_input.username))
            token = create_token({"sub":user_input.username},remember_me=user_input.remember_me)
            if user_input.remember_me:
                database.save_user_session_token(user_input.username,token)
            return UserLoginDataModel(user_name = user_data.username,user_surname = user_data.surname,user_photo = read_user_photo(user_data.username),auth_token = token,gender = user_data.gender)
    logger.warning("Wrong password or username %s:%s" % (user_input.username,user_input.password))
    return UserLoginDataModel()

@backend_api.post("/vixgon/api/login_with_token/{token}")
async def login_with_token(token: Annotated[str,Depends(validate_user_token)]) -> UserLoginDataModel:
    return database.get_username_from_token(token)
