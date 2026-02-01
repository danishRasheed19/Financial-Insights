from typing import Dict
from schemas.user_schema import RegisterRequest
from utils.security import hash_password

# Mock in-memory storage
mock_users: Dict[str, dict] = {}  # key = email

def create_user(user: RegisterRequest):
    if user.email in mock_users:
        return None
    mock_users[user.email] = {
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "hashed_password": hash_password(user.password)
    }
    return mock_users[user.email]

def get_user(email: str):
    return mock_users.get(email)
