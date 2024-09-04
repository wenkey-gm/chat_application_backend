from datetime import datetime
from typing import List

from pydantic import EmailStr, BaseModel

from src.models.message import Message


class MessageResponseModel(BaseModel):
    id: int
    content: str
    user_id: int
    timestamp: datetime

    class Config:
        orm_mode = True  # Enables compatibility with ORM objects


class MessageDto(BaseModel):
    email: EmailStr
    messages: List[MessageResponseModel]

    class Config:
        orm_mode = True
