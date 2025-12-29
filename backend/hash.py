from argon2 import PasswordHasher




argon2 = PasswordHasher()
def hash_pwd(data: str) -> str:
    try:
        hash = argon2.hash(data)
    except:
        return ""
    return hash