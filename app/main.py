"""
FastAPI Application Configuration

This module configures a FastAPI application instance (`app`) with middleware
and routers for handling API requests. It sets up CORS (Cross-Origin Resource
Sharing) middleware to allow cross-origin requests from any origin (`*`) and
configures API routes using the `api_router` imported from api.main.
"""


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.main import api_router


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix='/v1')
