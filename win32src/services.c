#define WIN32_LEAN_AND_MEAN
#include <windows.h>
#include <stdlib.h>
#include "include/error_handling.h"

typedef struct {
    DWORD BufferSize;
    DWORD ServicesCount;
    ENUM_SERVICE_STATUSW* Buffer;
    SC_HANDLE hServiceHandle;
} services_container_t;

SC_HANDLE CreateServiceInstance() {
    SC_HANDLE hServiceHandle = OpenSCManagerW(
        NULL,NULL,
        SC_MANAGER_ALL_ACCESS
    );
    if (hServiceHandle == NULL) {
        print_error(GetLastError());
    }
    return hServiceHandle;
}

BOOL GetBufferSize(SC_HANDLE hServiceHandle,services_container_t* container) {
    if (container == NULL || hServiceHandle == NULL ) { return 0; }
    BOOL enum_result = EnumServicesStatusW(
        hServiceHandle,
        SERVICE_WIN32,
        SERVICE_STATE_ALL,
        NULL,
        0,
        &container->BufferSize,
        &container->ServicesCount,
        NULL
    );
    DWORD errcode = GetLastError();
    if (errcode == ERROR_MORE_DATA) {
        return TRUE;
    }
    return FALSE;
}


__declspec(dllexport) void GetRunningServices(services_container_t* container) {
    SC_HANDLE hServiceHandle = CreateServiceInstance();
    if (hServiceHandle == NULL) { return; }
    BOOL get_buffer_size_result = GetBufferSize(hServiceHandle,container);
    if (!get_buffer_size_result) {
        printf("Cannot get buffer size :/");
        CloseServiceHandle(hServiceHandle);
        return;
    }
    container->Buffer = (ENUM_SERVICE_STATUSW*)malloc(container->BufferSize);
    if (container->Buffer == NULL) {
        printf("Cannot allocate memory :/\n");
        CloseServiceHandle(hServiceHandle);
        return;
    }
    BOOL enum_result = EnumServicesStatusW(
        hServiceHandle,
        SERVICE_WIN32,
        SERVICE_STATE_ALL,
        container->Buffer,
        container->BufferSize,
        &container->BufferSize,&container->ServicesCount,NULL);
    if (enum_result == FALSE) {
        free(container->Buffer);
        CloseServiceHandle(hServiceHandle);
        print_error(GetLastError());
    }
    container->hServiceHandle = hServiceHandle;
}
__declspec(dllexport) void CreateVixgonService(LPCWSTR serviceName,LPCWSTR displayName,LPCWSTR binPath) {
    if (serviceName == NULL || binPath == NULL) {
        printf("Invalid parameters\n");
        return;
    }
    SC_HANDLE hServiceHandle = CreateServiceInstance();
    if (hServiceHandle == NULL) { return; }
    if (CreateServiceW(
        hServiceHandle,
        serviceName,
        displayName,
        SC_MANAGER_CREATE_SERVICE,
        SERVICE_WIN32_SHARE_PROCESS,
        SERVICE_AUTO_START,
        SERVICE_ERROR_IGNORE,
        binPath,
        NULL,NULL,NULL,NULL,NULL) == NULL) { 
        print_error(GetLastError());
        return;
    }
    wprintf(L"Service %ls created\n",serviceName);
    CloseServiceHandle(hServiceHandle);
}

__declspec(dllexport) BOOL DeleteVixgonService(LPCWSTR serviceName) {
    if (serviceName == NULL) {
        printf("Bad service name :/\n");
        return FALSE;
    }
    SC_HANDLE hService = CreateServiceInstance();
    if (hService == NULL) { return FALSE; }
    SC_HANDLE hSubService = OpenServiceW(
        hService,
        serviceName,
        SC_MANAGER_ALL_ACCESS
    );
    if (hSubService == NULL) {
        print_error(GetLastError());
        CloseServiceHandle(hService);
        return FALSE;
    }
    BOOL result = DeleteService(hSubService);
    CloseServiceHandle(hSubService);
    CloseServiceHandle(hService);
    print_error(GetLastError());
    return result;
}
__declspec(dllexport) void DestroyBuffer(services_container_t* container) {
    if (container == NULL || container->Buffer == NULL) {
        printf("Bad container or buffer\n");
        return;
    }
    free(container->Buffer);
    CloseServiceHandle(container->hServiceHandle);
    printf("Well done buffer destroyed \n");
}
