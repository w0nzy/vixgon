import os
import time
import sys
sys.path.append(os.path.join(os.path.dirname(__file__),".."))
from backend.db import Database

db = Database("test_database.db")
db.init_db()
db.push_user(
    "yildiz_ece",
    b"Ece1234",
    "Ece",
    "Yıldız",
    "female",
    1,
    25,
    time.time(),
    b"_"
    )
db.extract_user("alperen")