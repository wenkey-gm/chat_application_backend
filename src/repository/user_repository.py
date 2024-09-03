from sqlalchemy import select
from sqlalchemy.orm import Session

from src.models.user import User


class UserRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_user(self, email: str, password: str) -> User:
        user = User(email=email, password=password)
        self.session.add(user)
        self.session.commit()
        self.session.refresh(user)
        return user

    def get_users(self):
        return self.session.query(User).all()

    def get_user_by_email(self, user_email: str) -> User:
        filtered_users_statement = select(User).filter_by(email=user_email)
        return self.session.scalars(filtered_users_statement).first()


