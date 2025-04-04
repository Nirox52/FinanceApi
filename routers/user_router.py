from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import user_crud
from database import SessionLocal

router = APIRouter(prefix="/users")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_user(telegram_id: int, db: Session = Depends(get_db)):
    return user_crud.create_user(db, telegram_id)

@router.get("/{telegram_id}")
def get_user(telegram_id: int, db: Session = Depends(get_db)):
    return user_crud.get_user_by_telegram_id(db, telegram_id)

@router.delete("/{telegram_id}")
def delete_user(telegram_id: int, db: Session = Depends(get_db)):
    return user_crud.delete_user_by_telegram_id(db, telegram_id)

