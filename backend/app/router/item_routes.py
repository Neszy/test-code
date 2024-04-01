from fastapi import APIRouter
from app.controllers.item_controller import router as item_controller_router

router = APIRouter()

router.include_router(item_controller_router, prefix="/images", tags=["items"])
