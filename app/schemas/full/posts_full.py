from typing import List, Optional

from pydantic import ConfigDict, Field

from app.schemas.base.posts_base import PostBase
from app.schemas.base.users_base import UserBase
from app.schemas.full.comments_full import CommentDB
from app.schemas.full.tags_full import TagDB


class PostCreate(PostBase):
    user_id: int
    tag_ids: List[int] = Field(default_factory=list)


class PostShortDB(PostBase):
    id: int
    user: Optional[UserBase]
    tags: Optional[List[TagDB]]

    model_config = ConfigDict(from_attributes=True)


class PostDB(PostBase):
    id: int
    user: Optional[UserBase]
    comments: List[CommentDB] = []
    tags: List[TagDB] = []

    model_config = ConfigDict(from_attributes=True)
