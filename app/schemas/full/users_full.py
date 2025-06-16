from typing import List

from pydantic import ConfigDict, Field

from app.schemas.base.comments_base import CommentBase
from app.schemas.base.posts_base import PostBase
from app.schemas.base.users_base import UserBase


class UserCreate(UserBase):
    pass


class UserDB(UserCreate):
    id: int
    posts: List[PostBase] = Field(default_factory=list)
    comments: List[CommentBase] = Field(default_factory=list)

    model_config = ConfigDict(from_attributes=True)
