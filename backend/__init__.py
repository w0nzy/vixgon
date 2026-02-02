import jwt
import secrets
from datetime import timedelta
from datetime import datetime
from datetime import timezone

from fastapi import (
    FastAPI,
    Depends,
    Header,
    Request,
    Response
    )
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import HTTPException
from argon2 import PasswordHasher

from backend.hash import compare_hash
from modules.error_handling import error
from backend.util import generate_item_path
from modules.vixgon_log import create_logger
from backend.util import read_user_photo, safeb64decode
from backend.models import LoginModel,TokenData,ItemCreateDataModel
from backend.db import Database, DatabaseRegisterCode, DatabaseUserRegisterModel
from backend.models import ShelfList, UserDataModel, UserLoginDataModel, UserRegistrationResponseModel
logger = create_logger()
backend_api = FastAPI()
argon2 = PasswordHasher()
database = Database("main.db")
database.init_db()
jwt_secret_key = "0b1211543e2971991cc26974b53e7a5b9adf00576d8d82c9de38e691b1b3110e"

def validate_user_token(header: Request):
    token_data = header
    if isinstance(header,Request):
        token_data = header.headers.get("Authorization")
        if token_data is None:
            raise HTTPException(status_code = 401,detail = "No token",headers = {"WWW-Authenticate":"Bearer"})

    try:
        jwt.decode(token_data,jwt_secret_key,algorithms=["HS256"])
    except Exception as e: # fix here
        logger.critical("Validation error %s" % (str(e)))
        raise HTTPException(status_code = 401,detail = "Expired token",headers = {"WWW-Authenticate":"Bearer"})
    return TokenData(token=token_data)
def create_token(payload: dict,remember_me = False) -> str:
    payload = payload.copy()
    payload.update({"exp":datetime.now(timezone.utc) + timedelta(minutes =1000000)})
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

@backend_api.post("/vixgon/api/login_with_token")
async def login_with_token(token = Depends(validate_user_token)) -> UserLoginDataModel:
    return database.get_username_from_token(token.token)
@backend_api.get("/vixgon/api/get_shelfs")
async def get_shelfs(response: Response,token = Depends(validate_user_token)) -> ShelfList:
    response.headers["action"] = "get-shelfs"
    return database.get_shelfs()

@backend_api.post("/vixgon/api/create_item")
async def create_item_data(data: ItemCreateDataModel) -> dict:
    if database.get_shelf_count(data.item_shelf) == 0:
        return {"bad_shelf":data.item_shelf}
    if not database.create_item(data.item_name,data.item_shelf,data.item_description,data.item_barcode,data.created_by_who):
        return {"cannot_create_item":data.item_shelf}
    return {"success":data.item_name}
@error(return_value={"status":"fail"})
@backend_api.post("/vixgon/api/add_item_photo")
async def save_photo(data: str,item_name: str,token = Depends(validate_user_token)) -> dict:
    print(database.get_item_count(item_name))
    if database.get_item_count(item_name) == 0:
        raise ValueError("Item name %s does not exist" % (item_name))
    with open(generate_item_path(item_name),"wb") as fd:
        fd.write(safeb64decode(data))
    return {"status":"success"}
@backend_api.post("/vixgon/api/add_item")
async def add_item(item_barcode: str,count: int,token = Depends(validate_user_token)) -> dict:
    if database.get_item_count(item_barcode) == 0:
        return {"no_item":item_barcode}
    return {"success":item_barcode} if database.add_item(item_barcode,count) else {"bad_item":item_barcode}

@backend_api.get("/vixgon/api/get_item/{item_barcode}")
async def get_item(item_barcode: str,get_photos = False) -> dict:
    if database.get_item_count(item_barcode) == 0:
        return {"no_item":item_barcode}
    return database.get_item(item_barcode,get_photos)