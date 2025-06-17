from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud.base import CRUDBase
from app.models.posts import Posts


class CRUDPosts(CRUDBase):

    async def get_all_posts(
            self,
            session: AsyncSession,
            status: str = None,
            include: Optional[list[str]] = None
    ) -> list[Posts]:
        query = select(Posts)
        if status:
            query = query.where(Posts.status == status)

        include = self._parse_include(include)

        if 'user' in include:
            query = query.options(selectinload(Posts.user))
        if 'tags' in include:
            query = query.options(selectinload(Posts.tags))

        db_data = await session.execute(query)
        posts = db_data.scalars().all()
        return posts

    async def get_post_by_id(
            self,
            post_id: int,
            session: AsyncSession,
            include: Optional[list[str]] = None
    ) -> Posts | None:
        query = select(Posts).where(Posts.id == post_id)
        include = self._parse_include(include)

        if 'user' in include:
            query = query.options(selectinload(Posts.user))
        if 'tags' in include:
            query = query.options(selectinload(Posts.tags))
        if 'comments' in include:
            query = query.options(selectinload(Posts.comments))

        db_data = await session.execute(query)
        post = db_data.scalars().first()

        return post


posts_crud = CRUDPosts(Posts)
