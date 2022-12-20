from typing import List

from fastapi import APIRouter
from ..models.orders import Orders


router = APIRouter(
    prefix="/orders"
)


@router.get('/', response_model=List[Orders])
def get_orders():
    return []
