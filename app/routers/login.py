
from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta

import app.database.user as user_helpers
import app.utils.auth as auth_utils
from app.constants import ACCESS_TOKEN_EXPIRE_MINUTES
from app.models import LoginResponse, User, UpdateUser

from .helpers import create_route_v1, create_response, oauth2_scheme


router = APIRouter()

@router.post(create_route_v1('login'), tags=['login'], response_model=LoginResponse, response_description='User login.')
async def login(data: OAuth2PasswordRequestForm = Depends()):
    email = data.username
    password = data.password

    user = await auth_utils.authenticate_user(email, password)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = auth_utils.create_access_token(
        data={"sub": str(user.id)}, expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return JSONResponse(
        status_code=status.HTTP_200_OK, 
        content=create_response(
            jsonable_encoder({
                'token': access_token,
                'user': jsonable_encoder(user)
            })
        )
    )

@router.get('/test/')
async def test(token: str = Depends(oauth2_scheme)):
    return 'hi'