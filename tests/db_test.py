import os
import time
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from backend.db import Database
import secrets
db = Database("main.db")
db.init_db()

db.close()