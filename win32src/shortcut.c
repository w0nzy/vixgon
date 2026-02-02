#include <ole2.h>
#include <shobjidl.h>
#include <stdio.h>

#define WIDE(l)(L##l)

#define STAT_OK 0xf
#define STAT_BAD 0xfffe
#define STAT_CO_INITALIZE_ERROR 0xff


__declspec(dllexport) short int CreateShortcut(LPCWSTR lnkPath,LPCWSTR binaryPath,LPCWSTR description) {
    if (FAILED(CoInitialize(NULL))) {
        return STAT_CO_INITALIZE_ERROR;
    }
    IShellLinkW* shellobj;
    IPersistFile* pf;
    int result = STAT_BAD;
    if (SUCCEEDED(CoCreateInstance(&CLSID_ShellLink,NULL,CLSCTX_INPROC_SERVER,&IID_IShellLinkW,(LPVOID*)&shellobj))) {
        shellobj->lpVtbl->SetPath(shellobj,binaryPath);
        shellobj->lpVtbl->SetDescription(shellobj,description == NULL ? L"" : description);
        if (
            SUCCEEDED(shellobj->lpVtbl->QueryInterface(shellobj,&IID_IPersistFile,(void**)&pf)) && 
            SUCCEEDED(pf->lpVtbl->Save(pf,lnkPath,TRUE))
            )
            {
                pf->lpVtbl->Release(pf);
                result = STAT_OK;
            }
        shellobj->lpVtbl->Release(shellobj);
        CoUninitialize();
    }
    return result;
}
int main() {
    CreateShortcut(WIDE("C:\\Users\\Ömer Çavuş\\test.lnk"),WIDE("C:\\Users\\Ömer Çavuş\\arc.py"),WIDE("Simple test"));
    return 0;
}