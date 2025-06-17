from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.users import users_crud
from app.schemas.full.users_full import UserDB

router = APIRouter(
    prefix='/api/users',
    tags=['Users'],
)


@router.get(
    '/{id}',
    response_model=UserDB,
    response_model_exclude_none=True,
)
async def get_user_by_id(
        id: int,
        include: list[str] | None = Query(None),
        session: AsyncSession = Depends(get_async_session),
):
    include = include or []
    user_db = await users_crud.get_user_by_id(id, session, include=include)
    if not user_db:
        raise HTTPException(status_code=404, detail="User not found")

    user = UserDB.model_validate(user_db)
    return user
