import ctypes
import ctypes.wintypes

from requests.auth import CONTENT_TYPE_MULTI_PART
from .vixgon_log import create_logger

logger = create_logger()

def geterrno() -> int:
    ctypes.windll.kernel32.GetLastError.restype = ctypes.wintypes.DWORD
    return ctypes.windll.kernel32.GetLastError()


def error(return_value = False):
    def decorator(function):
        def wrapper(*args, **kwargs):
            result = return_value
            try:
                result = function(*args, **kwargs)
            except Exception as err:
                logger.critical("Error %s" % (str(err)))
            return result
        return wrapper
    return decorator