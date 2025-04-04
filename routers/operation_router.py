from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from crud import operation_crud
from database import SessionLocal

router = APIRouter(prefix="/operations")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_operation(telegram_id: int, type: str, amount: float, description: str, db: Session = Depends(get_db)):
    return operation_crud.create_operation(db, telegram_id, type, amount, description)

@router.get("/{telegram_id}")
def get_operations(telegram_id: int, db: Session = Depends(get_db)):
    return operation_crud.get_operations_by_telegram_id(db, telegram_id)

@router.delete("/{operation_id}")
def delete_operation(operation_id: int, db: Session = Depends(get_db)):
    return operation_crud.delete_operation(db, operation_id)

