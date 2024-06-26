"""
Module defining API routes for managing Iris data.

This module initializes an APIRouter and includes routes related to Iris
data management. It imports and includes the 'iris'
router from the 'api.routes' module.
"""
from fastapi import APIRouter
from api.routes import iris

api_router = APIRouter()
api_router.include_router(iris.router, prefix="/iris", tags=["iris"])
