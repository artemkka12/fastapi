from fastapi import Depends, APIRouter, HTTPException, File, UploadFile
from sqlalchemy.orm import Session

from src.database import get_db
from . import service, schemas
from .exceptions import ItemNotFoundException
from ..users.service import get_user_by_id

router = APIRouter()


@router.post("", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(get_db)):
    if not get_user_by_id(db, user_id=item.user_id):
        raise HTTPException(status_code=400, detail=f"User with id {item.user_id} does not exist.")

    return service.create_item(db=db, item=item)


@router.post("/{id}/upload-image")
async def upload_image(item_id: int, image: UploadFile = File(...), db: Session = Depends(get_db)):
    return await service.upload_image(db=db, item_id=item_id, image=image)


@router.get("/{id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(get_db)):
    item = service.get_item_by_id(db, item_id=item_id)
    if not item:
        raise ItemNotFoundException(item_id=item_id)

    return item


@router.get("", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = service.list_items(db, skip=skip, limit=limit)
    return items
