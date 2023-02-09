import bcrypt
from sqlalchemy.orm import Session

from apps.users import models
from apps.users import schemas


def hash_password(password):
    password = password.encode()

    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password, salt)

    return hashed.decode()


# noinspection PyTypeChecker
def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


# noinspection PyTypeChecker
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    password = hash_password(user.password)
    db_user = models.User(email=user.email, hashed_password=password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
