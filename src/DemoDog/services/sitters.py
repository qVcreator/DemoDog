import datetime
from typing import List

from fastapi import Depends, HTTPException, status
from sqlalchemy.orm import Session

from .auth import AuthService
from .. import tables, models

from ..database import get_session


class SittersService:
    def __init__(self, session: Session = Depends(get_session),
                 auth_service: AuthService = Depends()):
        self.session = session
        self.auth_service = auth_service

    def _is_email_exist(self, email: str) -> bool:
        sitter = (
            self.session
            .query(tables.Sitter)
            .filter_by(email=email)
        )

        if not sitter:
            return True
        else:
            return False

    def create_sitter(
            self,
            create_sitter: models.CreateSitter
    ) -> models.Token:
        sitter = tables.Sitter(
            email=create_sitter.email,
            first_name=create_sitter.first_name,
            second_name=create_sitter.second_name,
            father_name=create_sitter.father_name,
            role=models.Role.SITTER,
            is_deleted=False,
            password=self.auth_service.hash_password(create_sitter.password),
        )

        if self._is_email_exist(sitter.email):
            raise HTTPException(status_code=status.HTTP_409_CONFLICT)

        self.session.add(sitter)
        self.session.commit()
        result = self.auth_service.create_token(sitter)
        return result

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
