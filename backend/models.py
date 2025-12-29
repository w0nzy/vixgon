from pydantic import BaseModel
from dataclasses import dataclass

from .enums import UserType


class LoginModel(BaseModel):
    username: str
    password: str

class UserLoginDataModel(BaseModel):
    auth_token: str
    user_photo: str

@dataclass
class UserRegistrationModel:
    name: str
    surname: str
    age: int
    user_type: int
    gender: str
    registration_time: int
    user_photo: str
