from fastapi import APIRouter
from . import users
# from . import user, products, auth, orders

router = APIRouter()

router.include_router(users.router, tags=["Users"], prefix="/users")