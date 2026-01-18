import os
import base64
from modules.vixgon_log import create_logger
from fastapi import Request, Response
logger = create_logger()

def get_user_photo(username: str) -> str:
    return os.path.join(os.path.join(os.path.dirname(__file__),"users",username)) + ".png"

def safeb64encode(content: bytes) -> bytes:
    try:
        data = base64.b64encode(content)
        logger.info("Data converted successfully to b64 format")
    except Exception as encode_error:
        logger.critical("Cannot encode data to b64 error is %s" % (str(encode_error)))
        return b""
    return data

def read_user_photo(username: str) -> bytes:
    photo_path = get_user_photo(username)
    if not os.path.exists(photo_path):
        logger.warning("User doesnt exists %s" % (username))
        return b""
    data = b""
    try:
        with open(photo_path,"rb") as fd:
            data = fd.read()
        logger.info("Photo readed(%s) size %s " % (photo_path,len(data)))
        data = safeb64encode(data)
    except Exception as err:
        logger.critical("Cannot read %s error is %s" % (photo_path,str(err)))
    return data.decode()
def sample_test(alperen: str):
    return alperen

def put_action_to_http_header(request: Request,response: Response) -> Response:
    response.headers["action"] = request.url.path[1:].replace("/","-")
    return response