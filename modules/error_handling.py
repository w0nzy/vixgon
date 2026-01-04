import ctypes
import ctypes.wintypes

from requests.auth import CONTENT_TYPE_MULTI_PART

def geterrno() -> int:
    ctypes.windll.kernel32.GetLastError.restype = ctypes.wintypes.DWORD
    return ctypes.windll.kernel32.GetLastError()