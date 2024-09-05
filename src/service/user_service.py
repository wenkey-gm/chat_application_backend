from src.DTO.user_dto import UserDto, UserResponseModel

from src.repository.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def get_user(self, user: UserDto) -> UserResponseModel:
        db_user = self.user_repository.get_user(user)
        if db_user is None:
            raise ValueError("User not found")
        return UserResponseModel(id=db_user.id, email=db_user.email, is_success=True)

