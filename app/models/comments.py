from sqlalchemy import Column, ForeignKey, String, Text
from sqlalchemy.orm import relationship

from app.core.db import Base


class Comments(Base):
    text = Column(Text, nullable=True)

    user_id = Column(String(36), ForeignKey("users.id"), nullable=False)
    post_id = Column(String(36), ForeignKey("posts.id"), nullable=False)

    user = relationship("Users", back_populates="comments")

    post = relationship("Posts", back_populates="comments")
