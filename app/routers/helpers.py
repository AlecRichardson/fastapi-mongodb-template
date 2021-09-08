from fastapi.security import OAuth2PasswordBearer
from typing import Any


def create_route_v1(route: str) -> str:
    return f'/api/v1/{route}'
    
def create_response(data: Any) -> dict:
    return {'data': data}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=create_route_v1('login'))
