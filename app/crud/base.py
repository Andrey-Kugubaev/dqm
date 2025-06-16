from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


class CRUDBase:

    def __init__(self, model):
        self.model = model

    async def get(
            self,
            obj_id: str,
            session: AsyncSession
    ):
        query = select(self.model).where(self.model.id == obj_id)
        db_data = await session.execute(query)
        return db_data.scalars().first()

    async def get_all(
            self,
            session: AsyncSession
    ):
        db_data = await session.execute(
            select(self.model)
        )
        return db_data.scalars().all()

    async def create(
            self,
            obj_id,
            session: AsyncSession
    ):
        pass

    async def update(
            self,
            db_obj,
            obj_in,
            session: AsyncSession,
    ):
        pass

    async def remove(
            self,
            db_obj,
            session: AsyncSession,
    ):
        pass
