from typing import List

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from ..models.orders import Orders


router = APIRouter(
    prefix="/orders"
)


@router.get('/', response_model=List[Orders])
def get_orders(auth_data: OAuth2PasswordRequestForm = Depends()):
    return []
