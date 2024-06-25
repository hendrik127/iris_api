from fastapi import APIRouter

from api.routes import iris

api_router = APIRouter()
api_router.include_router(iris.router, prefix="/iris", tags=["iris"])
