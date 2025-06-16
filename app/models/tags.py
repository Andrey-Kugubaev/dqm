from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from app.core.db import Base
from app.models.posts import post_tags


class Tags(Base):
    name = Column(String(128), nullable=True)
    posts = relationship("Posts", secondary=post_tags, back_populates="tags")
