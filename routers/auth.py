from fastapi import APIRouter, HTTPException, status
from schemas.user_schema import RegisterRequest, LoginRequest, AuthResponse
from utils.security import verify_password
from utils.jwt import create_access_token
from db.mock_user import create_user, get_user

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register", response_model=AuthResponse)
def register(payload: RegisterRequest):
    """
    Register a new user.
    """
    existing_user = get_user(payload.email)
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    user = create_user(payload)
    token = create_access_token({"sub": user["email"]})
    return {"access_token": token, "token_type": "bearer"}


@router.post("/login", response_model=AuthResponse)
def login(payload: LoginRequest):
    """
    Login user with email & password
    """
    user = get_user(payload.email)
    if not user or not verify_password(payload.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    token = create_access_token({"sub": user["email"]})
    return {"access_token": token, "token_type": "bearer"}
