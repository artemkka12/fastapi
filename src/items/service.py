import aiofiles
from fastapi import UploadFile
from sqlalchemy.orm import Session

from . import models, schemas
from .exceptions import ItemNotFoundException


# noinspection PyTypeChecker
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


async def upload_image(db: Session, item_id: int, image: UploadFile):
    item = get_item_by_id(db, item_id=item_id)
    if not item:
        raise ItemNotFoundException(item_id=item_id)

    async with aiofiles.open(f"images/{image.filename}", "wb") as f:
        while content := await image.read(1024):
            await f.write(content)

    item.image_path = f"images/{image.filename}"
    db.commit()
    db.refresh(item)

    return {"filename": image.filename}


# noinspection PyTypeChecker
def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Item).get(item_id)


def list_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()
