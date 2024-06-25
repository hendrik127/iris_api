from fastapi import APIRouter

from api.routes import iris

api_router = APIRouter()
# api_router.include_router(login.router, tags=["login"])
api_router.include_router(iris.router, prefix="/iris", tags=["iris"])
# api_router.include_router(utils.router, prefix="/utils", tags=["utils"])
# api_router.include_router(items.router, prefix="/items", tags=["items"])