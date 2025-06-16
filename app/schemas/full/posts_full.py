from typing import List, Optional

from app.schemas.base.posts_base import PostBase
from app.schemas.base.users_base import UserBase
from app.schemas.full.comments_full import CommentDB
from app.schemas.full.tags_full import TagDB


class PostCreate(PostBase):
    user_id: int
    tag_ids: Optional[List[int]] = []


class PostShortDB(PostBase):
    id: int
    user: Optional[UserBase]
    tags: Optional[List[TagDB]]

    model_config = {
        "from_attributes": True
    }


class PostDB(PostBase):
    id: int
    user: Optional[UserBase]
    comments: List[CommentDB] = []
    tags: List[TagDB] = []

    model_config = {
        "from_attributes": True
    }
