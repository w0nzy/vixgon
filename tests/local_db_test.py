import os
import sys
import base64
import secrets

from pydantic import Extra

sys.path.append(os.path.abspath("."))


from modules import get_assets_path
from modules.db import ClientDatabase

from modules.db_models import LocalCredentialsModel

db = ClientDatabase()
db.init_db()

data = LocalCredentialsModel(username="Alperen",token = secrets.token_hex(16),user_photo=base64.b64encode(open(get_assets_path("alperen.png"),"rb").read()))
db.push_user_login_credentials(user_data=data)

db.close()
extracted_data = db.extract_user_credentials()

print("Username is %s token is %s path is %s" % (extracted_data.username,extracted_data.token,extracted_data.user_photo_path))