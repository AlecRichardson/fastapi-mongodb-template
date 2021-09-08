from pydantic import BaseModel, Field, EmailStr
from typing import Optional

from .user import User


class LoginResponse(BaseModel):
    token: str = Field(...)
    user: User = Field(...)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    user_id: Optional[str] = None