#include <windef.h>
#include <stdio.h>
typedef struct {
    DWORD errcode;
    char* message;
} ErrorTable;

static ErrorTable table[] = {
    {
        .errcode = ERROR_ACCESS_DENIED,
        .message = "Bad privilage run as administrator"
    },
    {
        .errcode = ERROR_INVALID_HANDLE,
        .message = "Bad SC_HANDLE value please check handle NULL or NOT"
    },
    {
        .errcode = ERROR_INVALID_PARAMETER,
        .message = "Bad parameter given check parameters "
    },
    {
        .errcode = ERROR_DATABASE_DOES_NOT_EXIST,
        .message = "Invalid database its not exists"
    },
    {
        .errcode = ERROR_DUPLICATE_SERVICE_NAME,
        .message = "Duplicated service name "
    },
    {
        .errcode = ERROR_SERVICE_EXISTS,
        .message = "Service already exists"
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
