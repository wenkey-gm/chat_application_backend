from datetime import datetime
from typing import List

from pydantic import EmailStr, BaseModel


class MessageCreate(BaseModel):
    content: str
    user_id: int

    class Config:
        from_attributes = True


class MessageResponseModel(BaseModel):
    id: int
    content: str
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
