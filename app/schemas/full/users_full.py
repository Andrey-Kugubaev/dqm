from typing import List, Optional

from app.schemas.base.comments_base import CommentBase
from app.schemas.base.posts_base import PostBase
from app.schemas.base.users_base import UserBase


class UserCreate(UserBase):
    pass


class UserDB(UserCreate):
    id: int
    posts: Optional[List[PostBase]] = []
    comments: Optional[List[CommentBase]] = []

    model_config = {
        "from_attributes": True
    }
