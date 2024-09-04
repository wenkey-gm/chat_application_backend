from sqlalchemy import and_, select
from sqlalchemy.orm import Session

from src.DTO.user_dto import UserDto
from src.models.user import User


class UserRepository:

    def __init__(self, session: Session):
        self.session = session

    def get_user(self, user: UserDto) -> User:
        statement = select(User).where(
            and_(User.email == user.email, User.password == user.password)
        )
        user = self.session.scalars(statement).first()
        return user
