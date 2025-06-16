from enum import Enum
from typing import Optional

from pydantic import BaseModel


class PostStatus(str, Enum):
    DRAFT = 'draft'
    PUBLISHED = 'published'
    SCHEDULED = 'scheduled'
    HIDDEN = 'hidden'
    ARCHIVED = 'archived'
    MODERATION = 'moderation'
    REJECTED = 'rejected'
    DELETED = 'deleted'


class PostBase(BaseModel):
    title: str
    text: str
    status: PostStatus
    image: Optional[str]

    model_config = {"from_attributes": True}
