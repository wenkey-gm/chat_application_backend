from src.DTO.message_dto import MessageDto, MessageResponseModel, MessageCreate

from src.repository.message_repository import MessageRepository


class MessageService:
    def __init__(self, message_repository: MessageRepository):
        self.message_repository = message_repository

    def get_user_messages(self, email: str) -> MessageDto:

        db_user = self.message_repository.get_user_messages(email)
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
        message = self.message_repository.save_user_message(message)
        return MessageResponseModel(id=message.id,
                                    content=message.content,
                                    is_recieved=message.is_received,
                                    user_id=message.user_id,
                                    timestamp=message.timestamp, )
