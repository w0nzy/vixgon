import os
import base64
import uuid
def is_running_exe() -> bool:
    return globals().get("__compiled__",False)

def get_assets_path(*path: str) -> str:
    return os.path.join(
        os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "assets",*path)
    )


def get_app_path(*path: str) -> str:
    app_data_path = os.path.expandvars("%LocalAppData%")
    base_path = os.path.join(app_data_path,"vixgon")
    os.makedirs(base_path,exist_ok=True) # no exception throwed
    return os.path.join(base_path,*path)

def get_user_photo_path(user_photo: str) -> str:
    base_path = os.path.join(get_app_path(),"user_photo")
    os.makedirs(base_path,exist_ok=True)
    return os.path.join(base_path,user_photo + ".png")

def get_local_database_path() -> str:
    return get_app_path("local.db")

def can_decodeb64data(content: str | bytes) -> bool:
    if not isinstance(content,str) and not isinstance(content,bytes):
        return False
    content = content.encode() if isinstance(content,str) else content
    try:
        base64.b64decode(content)
    except:
        return False
    return True

def create_uuid() -> str:
    return uuid.uuid4().hex