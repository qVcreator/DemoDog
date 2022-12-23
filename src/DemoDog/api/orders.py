from typing import List

from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from .. import models
from ..models import Role
from ..services.orders import OrdersService
from ..services.role_checker import RoleChecker

router = APIRouter(
    prefix="/orders",
    tags=['orders']
)


@router.post('/', response_model=int)
def create_order(
        order_data: models.OrdersCreate,
        user: models.AuthUser = Depends(RoleChecker([Role.USER])),
        service: OrdersService = Depends()
):
    return service.create_order(order_data)


@router.get('/admin', response_model=List[models.OrdersOutput])
def get_orders(
        user: models.AuthUser = Depends(RoleChecker([Role.ADMIN])),
        service: OrdersService = Depends()
):
    return service.get_orders()


@router.get('/{order_id}', response_model=models.OrderOutput)
def get_order_by_id(
        order_id: int,
        user: models.AuthUser = Depends(RoleChecker([Role.ADMIN, Role.SITTER, Role.ADMIN])),
        service: OrdersService = Depends()
):
    return service.get_order_by_id(order_id)


@router.get('/', response_model=List[models.OrdersOutput])
def get_orders_by_current_user(
        user: models.AuthUser = Depends(RoleChecker([Role.USER, Role.SITTER])),
        service: OrdersService = Depends()
):
    return service.get_orders_by_current_user(user.id)
