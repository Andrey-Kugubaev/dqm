from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from app.crud.base import CRUDBase
from app.models.users import Users


class CRUDUsers(CRUDBase):

    async def get_user_by_id(
            self,
            user_id: int,
            session: AsyncSession,
            include: Optional[list[str]] = None
    ) -> Optional[Users]:
        query = select(Users).where(Users.id == user_id)
        include = self._parse_include(include)

        if 'posts' in include:
            query = query.options(selectinload(Users.posts))
        if 'comments' in include:
            query = query.options(selectinload(Users.comments))

        db_data = await session.execute(query)
        user = db_data.scalars().first()

        return user


users_crud = CRUDUsers(Users)
