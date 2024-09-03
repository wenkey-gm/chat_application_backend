from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from src.config.base import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password = Column(String(255), nullable=False)

    messages = relationship("Message", back_populates="user")

    def __repr__(self):
        return f"<User(id={self.id}, email='{self.email}')>"
