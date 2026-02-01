from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def hash_password(password: str) -> str:
    if not isinstance(password, str):
        raise ValueError("Password must be a string")
    if len(password.encode("utf-8")) > 72:
        raise ValueError("Password too long (max 72 bytes for bcrypt)")
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
