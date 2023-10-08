from app import crud
from app.api import deps
from app.models.user import User
from app.schemas.record import RecordGet
from app.schemas.response import ListOfEntityResponse
from app.utils import get_responses_description_by_codes
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession

router = APIRouter()


@router.get(
    '/',
    responses=get_responses_description_by_codes([401, 403]),
    response_model=ListOfEntityResponse[RecordGet],
)
async def get_records(
    db: AsyncSession = Depends(deps.async_get_db),
    current_user: User = Depends(deps.get_current_active_user),
    skip: int | None = Query(None),
    limit: int | None = Query(None),
):
    data = await crud.record.get_multi(db, skip=skip, limit=limit)

    return ListOfEntityResponse[RecordGet](data=data)
