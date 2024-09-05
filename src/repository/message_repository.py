from sqlalchemy import select
from sqlalchemy.orm import Session

from src.DTO.message_dto import MessageCreate
from src.models.message import Message
from src.models.user import User


class MessageRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_user_messages(self, email: str) -> User:
        statement = (
            select(User, Message)
            .join(Message, User.id == Message.user_id)
            .where(User.email.like(email))
        )
        user_info = self.session.scalars(statement).first()
        return user_info

    def save_user_message(self, message: MessageCreate) -> Message:
        db_message = Message(content=message.content, user_id=message.user_id, is_received=message.is_received)
        self.session.add(db_message)
        self.session.commit()
        self.session.refresh(db_message)
        return db_message
