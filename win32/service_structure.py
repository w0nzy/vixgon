import os
import ctypes
import ctypes.wintypes

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
        ("hServiceHandle",ctypes.c_voidp)
    ]

backend = ctypes.WinDLL(os.path.join(os.path.dirname(__file__),"service_handling.dll"))

GetRunningServices =  backend.GetRunningServices
DestroyBuffer =  backend.DestroyBuffer

GetRunningServices.argtypes = [ctypes.POINTER(service_container_t)]
DestroyBuffer.argtypes = [ctypes.POINTER(service_container_t)]

def get_running_services(container: service_container_t):
    GetRunningServices(ctypes.byref(container))
def destroy_buffer(container: service_container_t):
    DestroyBuffer(container)

if __name__ == "__main__":
    container = service_container_t()
    get_running_services(container)
    for num in range(container.ServicesCount):
        print("%d:%s" % (num + 1,container.Buffer[num].lpDisplayName))
    destroy_buffer(container)