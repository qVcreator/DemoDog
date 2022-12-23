from datetime import datetime
from enum import Enum

from pydantic import BaseModel

from DemoDog.models import OutputSitter
from DemoDog.models.users import OutputUser


class Services(str, Enum):
    WALK = 1
    OVEREXPOSE = 2


class Status(str, Enum):
    CREATED = 1
    IN_PROGRESS = 2
    FINISHED = 3
    CANCELED = 4


class OrdersCreate(BaseModel):
    id: int
    date_create: datetime
    date_update: datetime
    sitter_id: int
    user_id: int
    service_type: Services
    status: Status

    class Config:
        orm_mode = True


class OrdersOutput(BaseModel):
    date_create: datetime
    date_update: datetime
    sitter: OutputSitter
    user: OutputUser
    service_type: Services
    status: Status

    class Config:
        orm_mode = True


class OrderOutput(BaseModel):
    date_create: datetime
    date_update: datetime
    sitter: OutputSitter
    user: OutputUser
    service_type: Services
    status: Status

    class Config:
        orm_mode = True
