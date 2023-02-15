from fastapi import Depends, APIRouter
from sqlalchemy.orm import Session

from src.database import get_db, engine
from . import service, schemas, models
from .exceptions import UserAlreadyExistsException, UserNotFoundException

models.Base.metadata.create_all(bind=engine)

router = APIRouter()


@router.post("", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = service.get_user_by_email(db, email=user.email)
    if db_user:
        raise UserAlreadyExistsException(email=user.email)

    return service.create_user(db=db, user=user)


@router.get("", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = service.list_users(db, skip=skip, limit=limit)

    return users


@router.get("/{id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    user = service.get_user_by_id(db, user_id=user_id)
    if user is None:
        raise UserNotFoundException(user_id=user_id)

    return user
