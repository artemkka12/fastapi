from fastapi import APIRouter

from src.items.router import router as items_router
from src.users.router import router as users_router

main_router = APIRouter()

main_router.include_router(users_router, prefix="/users", tags=["users"])
main_router.include_router(items_router, prefix="/items", tags=["items"])
