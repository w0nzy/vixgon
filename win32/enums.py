from enum import IntEnum



class Com(IntEnum):
    STAT_OK = 0xf
    STAT_BAD = 0xfffe
    STAT_CO_INITALIZE_ERROR = 0xff
