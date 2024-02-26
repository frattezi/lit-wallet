from fastapi import APIRouter, Depends

from .controller import user as user_router

api = APIRouter()

api.include_router(
    user_router.router,
    prefix="/users",
    tags=["Users"],
)
