from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.DTO.user_dto import UserDto, UserResponseModel
from src.config.database import Database
from src.repository.user_repository import UserRepository
from src.service.user_service import UserService

user_router = APIRouter()


@user_router.post("/login/", response_model=UserResponseModel)
async def get_user(
        user: UserDto, db: Session = Depends(Database.get_session)
) -> UserResponseModel:
    user_service = UserService(user_repository=UserRepository(db))
    try:
        return user_service.get_user(user)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
