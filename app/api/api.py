from fastapi import APIRouter

from app import api
from app.api.endpoints.root import router as root_router

api_router = APIRouter()

api_router.include_router(root_router, tags=["root"])
