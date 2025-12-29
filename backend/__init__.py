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
from backend.models import UserLoginDataModel
from backend.models import LoginModel


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/vixgon/api/login")
backend_api = FastAPI()
argon2 = PasswordHasher()

jwt_secret_key = "0b1211543e2971991cc26974b53e7a5b9adf00576d8d82c9de38e691b1b3110e"
def verify_hash(pwd_hash: str,pwd: str) -> bool:
    try:
        argon2.verify(pwd_hash,pwd)
    except:
        return False
    return True

def validate_user_credentials(username: str,pwd_hash: str):
    if username != "alperen" and pwd_hash: pass
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