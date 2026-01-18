#include <windef.h>
#include <stdio.h>
typedef struct {
    DWORD errcode;
    char* message;
} ErrorTable;

static ErrorTable table[] = {
    {
        .errcode = 0x5,
        .message = "Bad privilage run as administrator"
    },
    {
        .errcode = 0x6,
        .message = "Bad SC_HANDLE value please check handle NULL or NOT"
    },
    {
        .errcode = 0x57,
        .message = "Bad parameter given check parameters "
    },
    {
        .errcode = 0x429,
        .message = "Invalid database its not exists"
    }  
};

int table_size = sizeof(table) / sizeof(table[0]);
__declspec(dllexport) int print_error(DWORD errcode)  {

    for (size_t i = 0;i < table_size;++i) {
        if (table[i].errcode == errcode) {
            printf("%lu -> %s\n",table[i].errcode,table[i].message);
            break;
        }
    }
    return errcode;
}
