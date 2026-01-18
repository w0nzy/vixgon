from fastapi import FastAPI, Request,Response,Depends
from pydantic import BaseModel
from urllib3 import response
from backend.util import decorator_name

api = FastAPI()
class ResponseModel(BaseModel):
    text: str 

def set_header(data: Response,req: Request):
    print(req.url.path)
    data.headers["action"] = req.url.path[1:].replace("_","-")
       
@api.post("/get_label")
async def handle(response = Depends(set_header),data: str = "no") -> ResponseModel:
    return ResponseModel(text = data)