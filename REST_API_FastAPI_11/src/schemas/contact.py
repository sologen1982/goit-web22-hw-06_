from datetime import date
from typing import Optional

from pydantic import BaseModel, EmailStr, Field


class ContactSchema(BaseModel):
    first_name: str = Field(min_length=3, max_length=50)
    last_name: str = Field(min_length=3, max_length=50)
    email: EmailStr
    phone: str = Field(max_length=13)
    birthday: date
    additional_info: str = Field(max_length=250)
    completed: Optional[bool] = False


class ContactUpdateSchema(ContactSchema):
    completed: bool


class ContactResponse(BaseModel):
    id: int = 1
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: date
    additional_info: str
    completed: bool

    class Config:
        from_attributes = True
