# service/user_service.py
from src.repository.user_repository import UserRepository


class UserService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def create_user(self, email: str, password: str):
        return self.user_repository.create_user(email, password)

    def get_users(self):
        return self.user_repository.get_users()

    def get_user_by_email(self, user_email: str):
        return self.user_repository.get_user_by_email(user_email)
