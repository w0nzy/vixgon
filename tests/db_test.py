import os
import time
import sys
import base64

sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from backend.db import Database
import secrets
db = Database("main.db")
db.init_db()
data = db.get_shelfs()
db.close()

for data in data.shelfs[:]:
    print(f"Shelf name {data['shelf_name']} Created by {data['created_by_who']} Creation time {time.ctime(data['time_epoch'])}")