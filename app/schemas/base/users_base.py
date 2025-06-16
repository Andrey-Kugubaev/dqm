from enum import Enum
from typing import Optional

from pydantic import BaseModel, EmailStr, Field, field_validator


class GenderValue(str, Enum):
    MALE = 'male'
    FEMALE = 'female'
    OTHER = 'other'


class UserBase(BaseModel):
    name: str
    surname: Optional[str]
    age: Optional[int] = Field(None, gt=14, le=99)
    gender: Optional[GenderValue]
    email: EmailStr

    @field_validator("name", "surname")
    def name_cant_be_numeric(cls, value: Optional[str]):
        if value is not None and value.isnumeric():
            raise ValueError("Name can't be a number")
        return value

    model_config = {"from_attributes": True}
