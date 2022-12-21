from fastapi import APIRouter
from .orders import router as orders_router
from .sitters import router as sitter_router
from .auth import router as auth_router

router = APIRouter()
router.include_router(orders_router)
router.include_router(sitter_router)
router.include_router(auth_router)