import os

from fastapi import FastAPI, Body, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

import motor.motor_asyncio
from typing import Optional, List

from .routers import user, login

app = FastAPI()

app.include_router(user.router)
app.include_router(login.router)

@app.on_event("startup")
async def startup():
    pass

