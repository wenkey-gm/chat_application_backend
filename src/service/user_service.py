# service/user_service.py
from typing import List

from src.DTO.message_dto import MessageDto, MessageResponseModel
from src.DTO.user_dto import UserDto
from src.models.message import Message
from src.repository.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user: UserDto) -> str:
        db_user = self.user_repository.get_user(user)
        if db_user is None:
            raise ValueError("User not found")
        return db_user.email

    def get_user_messages(self, email: str) -> MessageDto:
        print(email)
        db_user = self.user_repository.get_user_messages(email)
        if db_user is None:
            raise ValueError("User not found")

        message_response_list = [
            MessageResponseModel(
                id=message.id,
                content=message.content,
                user_id=message.user_id,
                timestamp=message.timestamp
            ) for message in db_user.messages
        ]

        return MessageDto(
            email=db_user.email,
            messages=message_response_list
        )
