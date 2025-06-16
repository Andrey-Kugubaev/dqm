from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.db import get_async_session
from app.crud.posts import posts_crud
from app.schemas.full.posts_full import PostDB, PostShortDB

router = APIRouter(
    prefix='/api/posts',
    tags=['Posts'],
)


@router.get(
    '/',
    response_model=List[PostShortDB],
    response_model_exclude_none=True,
)
async def get_posts(
        status: str = Query(""),
        include: list[str] = Query([]),
        session: AsyncSession = Depends(get_async_session),
):
    status_filter = status if status else None

    posts_db = await posts_crud.get_all_posts(
        session, status=status_filter, include=include
    )
    if not posts_db:
        raise HTTPException(status_code=404, detail="Posts not found")
    return [
        PostShortDB.model_validate(post, from_attributes=True)
        for post in posts_db
    ]


@router.get(
    '/{id}',
    response_model=PostDB,
    response_model_exclude_none=True,
)
async def get_posts_by_id(
        id: int,
        include: list[str] = Query([]),
        session: AsyncSession = Depends(get_async_session),
):
    post_db = await posts_crud.get_post_by_id(id, session, include=include)
    if not post_db:
        raise HTTPException(status_code=404, detail="User not found")

    post = PostDB.model_validate(post_db)
    return post
