from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship

from src.database import Base

__all__ = ["User"]


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, unique=True)
    password = Column(String)
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String)
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
