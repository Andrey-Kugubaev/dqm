from sqlalchemy import Column, ForeignKey, String, Table, Text
from sqlalchemy.orm import relationship

from app.core.db import Base

post_tags = Table(
    "post_tags",
    Base.metadata,
    Column("post_id", ForeignKey("posts.id"), primary_key=True),
    Column("tag_id", ForeignKey("tags.id"), primary_key=True),
)


class Posts(Base):
    title = Column(String(256), unique=True, nullable=False)
    text = Column(Text, nullable=False)
    status = Column(String(32), nullable=False)
    image = Column(Text, nullable=True)

    user_id = Column(String(36), ForeignKey("users.id"), nullable=False) # ToDo change to Integer
    user = relationship("Users", back_populates="posts")

    comments = relationship(
        "Comments", back_populates="post", cascade="all, delete-orphan"
    )

    tags = relationship("Tags", secondary=post_tags, back_populates="posts")
