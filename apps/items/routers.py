from fastapi import Depends, FastAPI, APIRouter
from sqlalchemy.orm import Session

from apps.items import models
from apps.items import schemas
from apps.items import crud
from config.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

router = APIRouter()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/{user_id}", response_model=schemas.Item)
def create_item_for_user(user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@router.get("", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
