from datetime import datetime
from typing import List

from pydantic import EmailStr, BaseModel


class MessageCreate(BaseModel):
    content: str
    is_received: bool
    user_id: int

    class Config:
        from_attributes = True


class MessageResponseModel(BaseModel):
    id: int
    content: str
    is_received: int
    user_id: int
    timestamp: datetime

    class Config:
        from_attributes = True


class MessageDto(BaseModel):
    id: int
    email: EmailStr
    messages: List[MessageResponseModel]

    class Config:
        from_attributes = True
