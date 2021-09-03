from fastapi import APIRouter, status
from fastapi.responses import JSONResponse

import app.database.user as user_helpers
from app.models.user import UserModel, UpdateUserModel
from typing import List

from .helpers import create_route_v1, create_response

router = APIRouter()


@router.get(create_route_v1('users/{user_id}'), tags=['users'], response_model=UserModel, response_description='Get user by ID.')
async def get_user(user_id: str):
    user = await user_helpers.get_user_by_id(user_id)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=create_response(user))

@router.get(create_route_v1('users'), tags=['users'], response_model=List[UserModel], response_description='Get all users.')
async def get_users():
    users = await user_helpers.get_users()
    return JSONResponse(status_code=status.HTTP_200_OK, content=create_response(users))

@router.post(create_route_v1('users'), tags=['users'], response_model=UserModel, response_description='Create new user.')
async def create_user(user: UserModel):
    user = await user_helpers.create_user(user)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=create_response(user))

@router.put(create_route_v1('users/{user_id}'), tags=['users'], response_model=UserModel, response_description='Update user by ID.')
async def update_user(user_id: str, data: UpdateUserModel):
    user = await user_helpers.update_user(user_id, data)
    return JSONResponse(status_code=status.HTTP_200_OK, content=create_response(user))
