# app/api/__init__.py

from fastapi import APIRouter
from .endpoints.recipes import router as recipes_router

api_router = APIRouter()

api_router.include_router(recipes_router, prefix="/recipes", tags=["recipes"])