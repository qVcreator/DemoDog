import datetime
from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .. import tables, models

from ..database import get_session


class SittersService:
    def __init__(self, session: Session = Depends(get_session)):
        self.session = session

    def create_sitter(
            self,
            create_sitter: models.CreateSitter
    ) -> int:
        sitter = tables.Sitter(**create_sitter.dict())
        sitter.date_create = datetime.datetime.now()
        sitter.is_deleted = False
        self.session.add(sitter)
        self.session.commit()
        return sitter.id

    def get_sitter_by_id(self, sitter_id: int) -> tables.Sitter:
        sitter = (
            self.session
            .query(tables.Sitter)
            .filter_by(id=sitter_id)
            .first()
        )

        if not sitter:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

        return sitter

    def get_sitters(self) -> List[tables.Sitter]:
        sitters = (
            self.session
            .query(tables.Sitter)
            .filter_by(is_deleted=False)
            .all()
        )
        return sitters

    def update_sitter(
            self,
            sitter_id: int,
            update_sitter: models.UpdateSitter,
    ):
        sitter = self.get_sitter_by_id(sitter_id)
        sitter.date_update = datetime.datetime.now()
        for field, value in update_sitter:
            setattr(sitter, field, value)
        self.session.commit()

    def delete_sitter(
            self,
            sitter_id: int
    ):
        sitter = self.get_sitter_by_id(sitter_id)
        sitter.is_deleted = True
        self.session.commit()

    def restore_sitter(
            self,
            sitter_id: int
    ):
        sitter = self.get_sitter_by_id(sitter_id)
        sitter.is_deleted = False
        self.session.commit()
