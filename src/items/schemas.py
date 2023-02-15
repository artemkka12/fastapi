from pydantic import BaseModel


class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    user_id: int


class Item(ItemBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
