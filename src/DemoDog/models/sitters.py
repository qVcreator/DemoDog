from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class Sitters(BaseModel):
    id: int
    first_name: str
    second_name: str
    father_name: Optional[str]
    date_create: Optional[datetime]
    date_update: Optional[datetime]

    class Config:
        orm_mode = True


class UpdateSitter(BaseModel):
    first_name: str
    second_name: str
    father_name: Optional[str]

    class Config:
        orm_mode = True


class CreateSitter(BaseModel):
    first_name: str
    second_name: str
    father_name: Optional[str]

    class Config:
        orm_mode = True
