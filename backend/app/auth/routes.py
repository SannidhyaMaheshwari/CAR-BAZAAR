from fastapi import APIRouter, Depends, HTTPException, status
from bson import ObjectId
from app.core.database import get_db
from app.users.models import UserCreate
from app.auth.services import create_user, authenticate_user

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post("/register")
def register_user(user: UserCreate):
    db = get_db()
    users = db["users"]

    if users.find_one({"email": user.email}):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    user_id = create_user(users, user.dict())
    return {"message": "User registered successfully", "user_id": user_id}


@router.post("/login")
def login_user(email: str, password: str):
    db = get_db()
    users = db["users"]

    user = authenticate_user(users, email, password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    return {
        "id": str(user["_id"]),
        "name": user["name"],
        "email": user["email"],
        "user_type": user["user_type"]

    }
