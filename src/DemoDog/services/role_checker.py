from typing import List

from fastapi import HTTPException, Depends

from .auth import get_current_user

from DemoDog import models


class RoleChecker:
    def __init__(self, roles: List[models.Role]):
        self.roles = roles

    def __call__(self, user: models.AuthUser =  Depends(get_current_user)) -> models.AuthUser:
        if user.role not in self.roles:
            raise HTTPException(status_code=403, detail="Operation not permitted")
        return user
