from fastapi import APIRouter
from dependancies.databases import connect_to_mysql as conn
router=APIRouter()

@router.get("/")
def home():
    return conn