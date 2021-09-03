from bson import ObjectId
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from .fields import PyObjectId


class UserModel(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    first_name: str = Field(...)
    last_name: str = Field(...)
    email: EmailStr = Field(...)

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jdoe@example.com",
            }
        }

class UpdateUserModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "first_name": "Jane",
                "last_name": "Doe",
                "email": "jdoe@example.com",
            }
        }
