from pydantic import BaseModel

from src.items.schemas import Item

__all__ = ["UserBase", "UserCreate", "User"]


class UserBase(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    phone: str | None = None
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
