from app.api.api_v1.endpoints import login, record, users
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(login.router, tags=["Авторизация"])
api_router.include_router(users.router, prefix="/users", tags=["Пользователи"])
api_router.include_router(record.router, prefix="/records", tags=["Записи"])
