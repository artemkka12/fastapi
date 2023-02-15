from sqlalchemy.orm import Session

from . import models, schemas


# noinspection PyTypeChecker
def create_item(db: Session, item: schemas.ItemCreate):
    db_item = models.Item(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item


# noinspection PyTypeChecker
def get_item_by_id(db: Session, item_id: int):
    return db.query(models.Item).get(item_id)


def list_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()