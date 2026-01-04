from enum import IntEnum
class DatabaseRegisterCode(IntEnum):
    USER_ALREADY_EXISTS = 0
    USER_CREATED_SUCCESSFULLY = 1
    BAD_PARAMETER_LIST = 2
    BAD_HASH_VALUE = 3
    SQL_ERROR = 4
    NOT_INITIALIZED_DATABASE = 5