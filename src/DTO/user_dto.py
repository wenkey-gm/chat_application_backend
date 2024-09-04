from pydantic import BaseModel, EmailStr


class UserDto(BaseModel):
    email: EmailStr
    password: str

    class Config:
        from_attributes = True


class UserResponseModel(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True
