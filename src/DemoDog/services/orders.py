from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from DemoDog import tables, models
from DemoDog.database import get_session
from DemoDog.models import OrdersCreate, Role
from DemoDog.models.orders import Status


class OrdersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_order(self, order_data: OrdersCreate) -> int:
        order_data.status = Status.CREATED
        order = tables.Order(**order_data.dict())
        self.session.add(order)
        self.session.commit()
        return order.id

    def get_orders(self) -> List[tables.Order]:
        orders = (
            self.session
            .query(tables.Order)
            .all()
        )
        return orders

    def get_order_by_id(
            self,
            order_id: int,
            current_user: models.AuthUser) -> tables.Order:
        order = (
            self.session
            .query(tables.Order)
            .first()
        )

        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        if (current_user.role != Role.ADMIN or
                current_user.id != order.user_id or
                current_user.id != order.sitter_id):
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

        return order

    def get_orders_by_current_user(self,
                                   user_id: int) -> List[tables.Order]:
        orders = (
            self.session
            .query(tables.Order)
            .filter_by(user_id=user_id)
            .all()
        )
        return orders
