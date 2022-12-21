from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from DemoDog.models import Role


class BaseUser(BaseModel):
    id: int
    email: str
    password: str
    first_name: str
    second_name: str
    father_name: Optional[str]
    date_create: Optional[datetime]
    date_update: Optional[datetime]
    role: Role

    class Config:
        orm_mode = True


class Sitters(BaseUser):
    class Config:
        orm_mode = True


class UpdateSitter(BaseModel):
    first_name: str
    second_name: str
    father_name: Optional[str]

    class Config:
        orm_mode = True


class BaseCreateUser(BaseModel):
    email: str
    password: str
    first_name: str
    second_name: str
    father_name: Optional[str]

    class Config:
        orm_mode = True


class CreateUser(BaseCreateUser):
    class Config:
        orm_mode = True

