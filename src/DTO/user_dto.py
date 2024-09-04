from pydantic import BaseModel, EmailStr


class UserDto(BaseModel):
    email: EmailStr
    password: str

    class Config:
        orm_mode = True
