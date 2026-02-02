import os
import sys
import ctypes
import ctypes.wintypes

from .enums import Com
class SERVICE_STATUS(ctypes.Structure):
    _fields_ = [
        ("dwServiceType",ctypes.wintypes.DWORD),
        ("dwCurrentState",ctypes.wintypes.DWORD),
        ("dwControlsAccepted",ctypes.wintypes.DWORD),
        ("dwWin32ExitCode",ctypes.wintypes.DWORD),
        ("dwServiceSpecificExitCode",ctypes.wintypes.DWORD),
        ("dwCheckPoint",ctypes.wintypes.DWORD),
        ("dwWaitHint",ctypes.wintypes.DWORD)
    ]

class ENUM_SERVICE_STATUSW(ctypes.Structure):
    _fields_ = [
        ("lpServiceName",ctypes.wintypes.LPWSTR),
        ("lpDisplayName",ctypes.wintypes.LPWSTR),
        ("ServiceStatus",SERVICE_STATUS)
     ]

class service_container_t(ctypes.Structure):
    _fields_ = [
        ("BufferSize",ctypes.wintypes.DWORD),
        ("ServicesCount",ctypes.wintypes.DWORD),
        ("Buffer",ctypes.POINTER(ENUM_SERVICE_STATUSW)),
        ("hServiceHandle",ctypes.wintypes.SC_HANDLE)
    ]

backend = ctypes.WinDLL(os.path.join(os.path.dirname(__file__),"_win32_backend.dll"))

GetRunningServices =  backend.GetRunningServices
DestroyBuffer =  backend.DestroyBuffer
CreateVixgonService = backend.CreateVixgonService
DeleteVixgonService = backend.DeleteVixgonService
CreateShortcut = backend.CreateShortcut

GetRunningServices.argtypes = [ctypes.POINTER(service_container_t)]
DestroyBuffer.argtypes = [ctypes.POINTER(service_container_t)]
CreateVixgonService.argtypes = [ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR]
DeleteVixgonService.argtype = [ctypes.wintypes.LPCWSTR]
DeleteVixgonService.restype = ctypes.wintypes.BOOL
CreateShortcut.argtypes = [ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR,ctypes.wintypes.LPCWSTR]
CreateShortcut.restype = ctypes.c_int

def get_running_services(container: service_container_t):
    GetRunningServices(ctypes.byref(container))
def destroy_buffer(container: service_container_t):
    DestroyBuffer(container)
def create_vixgon_service(service_name: str,service_display_name: str,binPath: str) -> bool:
    return CreateVixgonService(service_name,service_display_name,binPath)
def delete_vixgon_service(service_name: str) -> bool:
    """
    Note: requires service name not display name
    """
    return DeleteVixgonService(service_name)
def create_shortcut(lnk_path,binary_path,description) -> int:
    result = CreateShortcut(lnk_path,binary_path,description)
    return next((obj for obj in Com if obj.value == result),0)
if __name__ == "__main__":
    container = service_container_t()
    get_running_services(container)
    create_vixgon_service("vixgon_postgres_server","Vixgon Postgres Sunucusu","pg_ctl.exe")
    for num in range(container.ServicesCount):
        if container.Buffer[num].lpServiceName == "vixgon_postgres_server":
            print("Servis mevcut peki Sunucu Çalışıyor mu ?:","Evet " if container.Buffer[num].ServiceStatus.dwCurrentState & 0x00000004 else "Hayır")
    destroy_buffer(container)