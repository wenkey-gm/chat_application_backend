from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.service.user_service import UserService
from src.repository.user_repository import UserRepository
from src.config.database import Database

user_router = APIRouter()


@user_router.post("/users/")
async def create_user(email: str, password: str, db: Session = Depends(Database.get_session)):
    user_service = UserService(user_repository=UserRepository(db))
    print("Hello world" + email + password)
    return user_service.create_user(email=email, password=password)


@user_router.get("/users/")
async def get_users(db: Session = Depends(Database.get_session)):
    user_service = UserService(user_repository=UserRepository(db))
    return user_service.get_users()
