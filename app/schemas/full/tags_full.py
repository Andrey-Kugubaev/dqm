from pydantic import ConfigDict

from app.schemas.base.tags_base import TagBase


class TagCreate(TagBase):
    pass


class TagDB(TagCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
