from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.DTO.message_dto import MessageDto
from src.DTO.user_dto import UserDto
from src.models.user import User
from src.service.user_service import UserService
from src.repository.user_repository import UserRepository
from src.config.database import Database

user_router = APIRouter()


@user_router.post("/login/", response_model=str)
async def get_user(user: UserDto, db: Session = Depends(Database.get_session)) -> str:
    user_service = UserService(user_repository=UserRepository(db))
    try:
        return user_service.get_user(user)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@user_router.get("/{email_id}/messages", response_model=MessageDto)
async def get_user_messages(email_id: str, db: Session = Depends(Database.get_session)):
    user_service = UserService(user_repository=UserRepository(db))
    try:
        return user_service.get_user_messages(email_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
