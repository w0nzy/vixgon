from enum import IntEnum

class UserType(IntEnum):
    USER_TYPE_GUEST = 0 # only the specified invisible to the naked eye
    USER_TYPE_WORKER = 1 # It can process data but cannot register new members.
    USER_TYPE_ADMIN = 2 # It can do everything: new member registration/member deletion, stock processing.

class DatabaseRegisterCode(IntEnum):
    USER_ALREADY_EXISTS = 0
    USER_CREATED_SUCCESSFULLY = 1
    BAD_PARAMETER_LIST = 2
    BAD_HASH_VALUE = 3
    SQL_ERROR = 4
    NOT_INITIALIZED_DATABASE = 5