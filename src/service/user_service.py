# service/user_service.py


from src.DTO.message_dto import MessageDto, MessageResponseModel, MessageCreate

from src.DTO.user_dto import UserDto, UserResponseModel

from src.repository.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user: UserDto) -> UserResponseModel:
        db_user = self.user_repository.get_user(user)
        if db_user is None:
            raise ValueError("User not found")
        return UserResponseModel(id=db_user.id, email=db_user.email)

    def get_user_messages(self, email: str) -> MessageDto:

        db_user = self.user_repository.get_user_messages(email)
        if db_user is None:
            raise ValueError("User not found")

        message_response_list = [
            MessageResponseModel(
                id=message.id,
                content=message.content,
                is_recieved=message.is_received,
                user_id=message.user_id,
                timestamp=message.timestamp,
            )
            for message in db_user.messages
        ]

        return MessageDto(
            id=db_user.id, email=db_user.email, messages=message_response_list
        )

    def save_user_message(self, message: MessageCreate) -> MessageResponseModel:
        message = self.user_repository.save_user_message(message)
        return MessageResponseModel(id=message.id,
                                    content=message.content,
                                    is_recieved=message.is_received,
                                    user_id=message.user_id,
                                    timestamp=message.timestamp, )
