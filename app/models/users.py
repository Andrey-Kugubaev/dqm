from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.core.db import Base


class Users(Base):
    name = Column(String(256), nullable=False)
    surname = Column(String(256), nullable=False)
    age = Column(Integer, nullable=True)
    gender = Column(String(8), nullable=True)
    email = Column(String(128), nullable=False) # ToDo unique=True, index=True

    posts = relationship(
        "Posts",
        back_populates="user",
        cascade="all, delete-orphan"
    )
    comments = relationship(
        "Comments",
        back_populates="user",
        cascade="all, delete-orphan"
    )
