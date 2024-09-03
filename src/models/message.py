from sqlalchemy import Column, Integer, String, DateTime, func

from src.config.base import Base


class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    def __repr__(self):
        return f"<Message(id={self.id}, content='{self.content}', timestamp={self.timestamp})>"
