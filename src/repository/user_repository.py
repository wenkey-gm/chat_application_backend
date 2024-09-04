from sqlalchemy import and_, select
from sqlalchemy.orm import Session

from src.DTO.user_dto import UserDto
from src.models.message import Message
from src.models.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_user(self, user: UserDto) -> User:
        statement = select(User).where(and_(User.email == user.email, User.password == user.password))
        user_info = self.session.scalars(statement).first()
        return user_info

    def get_user_messages(self, email: str) -> User:
        statement = (select(User, Message).join(Message, User.id == Message.user_id)
                     .where(User.email.like(email)))
        user_info = self.session.scalars(statement).first()
        return user_info
