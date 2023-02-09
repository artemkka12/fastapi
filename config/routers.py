from fastapi import APIRouter

from apps.users.routers import router as users_router
from apps.items.routers import router as items_router

router = APIRouter()

router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(items_router, prefix="/items", tags=["items"])
