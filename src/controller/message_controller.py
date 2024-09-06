from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.DTO.message_dto import MessageDto, MessageCreate, MessageResponseModel
from src.config.database import Database
from src.repository.message_repository import MessageRepository
from src.service.messsage_service import MessageService

message_router = APIRouter()


@message_router.get("/{token}/messages", response_model=MessageDto)
async def get_user_messages(token: str, db: Session = Depends(Database.get_session)):
    message_service = MessageService(message_repository=MessageRepository(db))
    try:
        return message_service.get_user_messages(token)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error occurred: {str(e)}")


@message_router.post("/{token}/message/", status_code=201, response_model=MessageResponseModel)
def create_message(token: str,message: MessageCreate, db: Session = Depends(Database.get_session)):
    message_service = MessageService(message_repository=MessageRepository(db))
    try:
        return message_service.save_user_message(message, token)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except SQLAlchemyError as e:
        raise HTTPException(status_code=500, detail=f"Database error occurred: {str(e)}")

