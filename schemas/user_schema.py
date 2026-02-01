from pydantic import BaseModel, EmailStr

# Request schemas
class RegisterRequest(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    password: str

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

# Response schemas
class AuthResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
