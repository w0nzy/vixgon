from pydantic import BaseModel
from dataclasses import dataclass
from dataclasses import field as Field

from .enums import UserType


class LoginModel(BaseModel):
    username: str
    password: str

class UserLoginDataModel(BaseModel):
    auth_token: str
    user_photo: str


class UserRegistrationModel(BaseModel):
    username: str
    password: str
    name: str
    surname: str
    gender: str
    age: int
    user_type: int
    registertration_time: int
    user_photo_name: str

class UserRegistrationResponseModel(BaseModel):
    detail: str

@dataclass
class DatabaseUserRegisterModel:
    username: str = Field(default="no_username")
    password: str =  Field(default="no_password")
    name: str = Field(default="no_name")
    surname: str = Field(default="no_surname")
    gender: str = Field(default="no_gender")
    age: int = Field(default=0)
    user_type: int = Field(default=-1)
    registertration_time: int = Field(default=0)
    user_photo_name: str = Field(default="no_photo")

