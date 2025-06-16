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
            include: list[str] = None
    ):
        query = select(Users).where(Users.id == user_id)
        if include is None:
            include = []
        elif len(include) == 1 and ',' in include[0]:
            include = include[0].split(',')

        if 'posts' in include:
            query = query.options(selectinload(Users.posts))
        if 'comments' in include:
            query = query.options(selectinload(Users.comments))

        db_data = await session.execute(query)
        user = db_data.scalars().first()

        return user


users_crud = CRUDUsers(Users)
