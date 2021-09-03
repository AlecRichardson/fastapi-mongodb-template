from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder

from app.models import UserModel, UpdateUserModel
from typing import List

from . import db

users_collection = db.get_collection('users')


async def get_users() -> List[UserModel]:
    return await users_collection.find().to_list(1000)

async def get_user_by_id(user_id: str) -> UserModel:
    user = await users_collection.find_one({'_id': user_id})

    if user:
        return user

async def create_user(user: UserModel) -> UserModel:
    inserted_user = await users_collection.insert_one(jsonable_encoder(user))
    created_user = await users_collection.find_one({"_id": inserted_user.inserted_id})

    if created_user:
        return created_user

    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

async def update_user(user_id: str, data: UpdateUserModel) -> UserModel:
    user = await users_collection.find_one({'_id': user_id})

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    updated_user = await users_collection.update_one(
        {'_id': user_id},
        {'$set': jsonable_encoder(data)}
    )
    return await users_collection.find_one({"_id": user_id})
