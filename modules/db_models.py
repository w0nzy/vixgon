from dataclasses import dataclass
from dataclasses import field
@dataclass
class LocalCredentialsModel:
    username: str = field(default="no_name")
    token: str = field(default="no_token")
    user_photo: str | bytes = field(default="no_data")
    user_photo_path: str = field(default = "no_path")