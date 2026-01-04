from pydantic import BaseModel
from dataclasses import dataclass
from dataclasses import field as Field


class LoginModel(BaseModel):
    username: str
    password: str

class UserLoginDataModel(BaseModel):
    auth_token: str
    user_name: str
    user_surname: str
    user_photo: str


class UserDataModel(BaseModel):
    username: str = Field(default = "no_username")
    password: str = Field(default="no_password")
    name: str = Field(default="no_name")
    surname: str = Field(default="no_surname")
    gender: str = Field(default="no_gender")
    age: int = Field(default = 0)
    user_type: int = Field(default = -1)
    registertration_time: int = Field(default =-1)
    user_photo_data: str = Field(default = "no_photo")

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

