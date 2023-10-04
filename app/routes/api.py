from fastapi import APIRouter
from endpoints import product_service, user_service

router = APIRouter()
router.include_router(product_service.router)
router.include_router(user_service.router)
