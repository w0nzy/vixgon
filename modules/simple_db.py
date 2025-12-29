import json
from typing import dataclass_transform

def load_db(file_path):
    try:
        fd = open(file_path,"r")
    except Exception as fd_error:
        print("Cannot open file:", fd_error)
    data = fd.read()
    fd.close()
    try:
        data = json.loads(data)
    except Exception as json_error:
        print("JSON decode error:", json_error)
        data = None
    return data

def save_db(file_path, data):
    try:
        fd = open(file_path,"w")
    except Exception as fd_error:
        print("Cannot open file:", fd_error)
    fd.write(json.dumps(data, indent=4))
    fd.close()