from datetime import datetime
from typing import Literal
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    password: str = Field(..., min_length=6)
    user_type: Literal["individual", "dealer"]


class UserInDB(BaseModel):
    id: str
    name: str
    email: EmailStr
    user_type: str
    created_at: datetime
