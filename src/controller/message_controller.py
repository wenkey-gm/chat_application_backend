from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from src.DTO.message_dto import MessageDto, MessageCreate, MessageResponseModel
from src.config.database import Database
from src.repository.message_repository import MessageRepository
from src.service.messsage_service import MessageService

message_router = APIRouter(
    prefix='/api/'
)


@message_router.get("/{email_id}/messages", response_model=MessageDto)
async def get_user_messages(email_id: str, db: Session = Depends(Database.get_session)):
    message_service = MessageService(message_repository=MessageRepository(db))
    try:
        return message_service.get_user_messages(email_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))


@message_router.post("/message/", status_code=201, response_model=MessageResponseModel)
def create_message(message: MessageCreate, db: Session = Depends(Database.get_session)):
    message_service = MessageService(message_repository=MessageRepository(db))
    try:
        return message_service.save_user_message(message)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
