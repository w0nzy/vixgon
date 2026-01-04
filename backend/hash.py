from argon2 import PasswordHasher




argon2 = PasswordHasher()
def hash_pwd(data: str) -> str:
    try:
        hash = argon2.hash(data)
    except:
        return ""
    return hash


def compare_hash(pwd: str,hash: str) -> str:
    try:
        argon2.verify(hash,pwd)
    except:
        return False
    return True