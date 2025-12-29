from enum import IntEnum

class UserType(IntEnum):
    USER_TYPE_GUEST = 0 # only the specified invisible to the naked eye
    USER_TYPE_WORKER = 1 # It can process data but cannot register new members.
    USER_TYPE_ADMIN = 2 # It can do everything: new member registration/member deletion, stock processing.