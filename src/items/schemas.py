from pydantic import BaseModel

__all__ = ["ItemBase", "Item", "ItemCreate"]


class ItemBase(BaseModel):
    title: str
    description: str | None = None
    price: int | None = None
    sku: str | None = None
    image_path: str | None = None


class ItemCreate(ItemBase):
    user_id: int


class Item(ItemBase):
    id: int

    class Config:
        orm_mode = True
