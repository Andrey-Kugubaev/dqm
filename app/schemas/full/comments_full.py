from pydantic import ConfigDict

from app.schemas.base.comments_base import CommentBase


class CommentCreate(CommentBase):
    user_id: int
    post_id: int


class CommentDB(CommentCreate):
    id: int

    model_config = ConfigDict(from_attributes=True)
