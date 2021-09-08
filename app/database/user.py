from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder
from pydantic import SecretBytes
from typing import List

from app.models import User, UpdateUser
from app.utils.auth import hash_password

from . import db

users_collection = db.get_collection('users')


async def get_users() -> List[User]:
    users = await users_collection.find().to_list(1000)
    return users

async def get_user_by_id(user_id: str) -> User:
    user = await users_collection.find_one({'_id': user_id})

    if user:
        return user


async def get_user_by_email(email: str) -> User:
    user = await users_collection.find_one({'email': email})
    
    if not user:
        raise Exception('Not found.')
        
    return User(**user)


async def create_user(user: User) -> User:
    user.password = str.encode(hash_password(user.password.get_secret_value()))
    user = jsonable_encoder(user)

    inserted_user = await users_collection.insert_one(user)
    created_user = await users_collection.find_one({"_id": inserted_user.inserted_id})
    
    if created_user:
        return user

    raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal Server Error")

async def update_user(user_id: str, data: UpdateUser) -> User:
    user = await users_collection.find_one({'_id': user_id})

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User not found.")

    updated_user = await users_collection.update_one(
        {'_id': user_id},
        {'$set': jsonable_encoder(data)}
    )
    user = await users_collection.find_one({"_id": user_id})

    return user
