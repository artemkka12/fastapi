from sqlalchemy.orm import Session

from . import models, schemas
from .utils import hash_password


def create_user(db: Session, user: schemas.UserCreate):
    password = hash_password(user.password)
    db_user = models.User(email=user.email, password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


# noinspection PyTypeChecker
def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).get(user_id)


# noinspection PyTypeChecker
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def list_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()
