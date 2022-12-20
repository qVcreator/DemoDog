from datetime import datetime
from enum import Enum

from pydantic import BaseModel


class Services(str, Enum):
    WALK = 1
    OVEREXPOSE = 2


class Status(str, Enum):
    CREATED = 1
    IN_PROGRESS = 2
    FINISHED = 3


class Orders(BaseModel):
    id: int
    date_create: datetime
    date_update: datetime
    sitter_id: int
    user_id: int
    service_type: Services
    status: Status

    class Config:
        orm_mode = True
