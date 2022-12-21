from typing import List

from fastapi import Depends, APIRouter, status, Response

from .. import models
from ..models.users import Sitters
from ..services.sitters import SittersService

router = APIRouter(
    prefix="/sitters",
    tags=['sitters']
)


@router.post('/', response_model=int)
def create_sitter(
        sitter_data: models.BaseCreateUser,
        sitters_service: SittersService = Depends()
):
    return sitters_service.create_sitter(sitter_data)


@router.get('/{sitter_id}', response_model=Sitters)
def get_sitter_by_id(
        sitter_id: int,
        sitters_service: SittersService = Depends()
):
    return sitters_service.get_sitter_by_id(sitter_id)


@router.get('/', response_model=List[Sitters])
def get_sitters(sitters_service: SittersService = Depends()):
    return sitters_service.get_sitters()


@router.put(
    '/{sitter_id}',
    status_code=status.HTTP_204_NO_CONTENT
)
def update_sitter(
        sitter_id: int,
        update_sitter: models.UpdateSitter,
        sitters_service: SittersService = Depends()
):
    sitters_service.update_sitter(sitter_id, update_sitter)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.delete('/{sitter_id}')
def delete_sitter(
        sitter_id: int,
        sitters_service: SittersService = Depends()
):
    sitters_service.delete_sitter(sitter_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.patch('/{sitter_id}')
def restore_sitter(
        sitter_id: int,
        sitters_service: SittersService = Depends()
):
    sitters_service.restore_sitter(sitter_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
