from typing import Generic, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeMeta

ModelType = TypeVar("ModelType", bound=DeclarativeMeta)


class CRUDBase(Generic[ModelType]):

    def __init__(self, model: Type[ModelType]):
        self.model = model

    async def get(
            self,
            obj_id: id,
            session: AsyncSession
    ) -> Optional[ModelType]:
        query = select(self.model).where(self.model.id == obj_id)
        db_data = await session.execute(query)
        return db_data.scalars().first()

    async def get_all(
            self,
            session: AsyncSession
    ) -> list[ModelType]:
        db_data = await session.execute(
            select(self.model)
        )
        return db_data.scalars().all()

    async def create(
            self,
            obj_in,
            session: AsyncSession
    ) -> ModelType:
        pass

    async def update(
            self,
            db_obj: ModelType,
            obj_in,
            session: AsyncSession,
    ) -> ModelType:
        pass

    async def remove(
            self,
            db_obj: ModelType,
            session: AsyncSession,
    ) -> ModelType:
        pass

    def _parse_include(self, include: Optional[list[str]]) -> list[str]:
        if include is None:
            return []
        if len(include) == 1 and ',' in include[0]:
            return include[0].split(',')
        return include
