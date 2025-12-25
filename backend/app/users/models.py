from datetime import datetime
from typing import Literal
from pydantic import BaseModel, EmailStr, Field


class UserCreate(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    password: str = Field(..., min_length=6)
    role: Literal["buyer", "seller"]


class UserInDB(BaseModel):
    id: str
    name: str
    email: EmailStr
    role: str
    created_at: datetime
