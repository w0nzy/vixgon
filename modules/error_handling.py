import ctypes
import traceback
import ctypes.wintypes

from requests.auth import CONTENT_TYPE_MULTI_PART
from .vixgon_log import create_logger
from typing import Any
logger = create_logger()

def geterrno() -> int:
    ctypes.windll.kernel32.GetLastError.restype = ctypes.wintypes.DWORD
    return ctypes.windll.kernel32.GetLastError()


def error(return_value: Any):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = return_value
            try:
                result = function(*args, **kwargs)
            except Exception as err:
                logger.exception(str(err),exc_info = True)
            return result
        return wrapper
    return decorator