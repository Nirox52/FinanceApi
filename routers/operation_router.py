from typing import List
from fastapi import APIRouter, Depends, Query,HTTPException
from sqlalchemy.orm import Session
from crud import operation_crud
from database import SessionLocal
from models.operations import Operations
from models.operation_schema import OperationCreateSchema, OperationSchemaBase, OperationUpdateSchema
from datetime import datetime

router = APIRouter(prefix="/operations")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/",tags=["Operations"])
def create_operation(operation: OperationCreateSchema, db: Session = Depends(get_db)):
    return operation_crud.create_operation(db, operation.telegram_id, operation.type, operation.amount, operation.description)


@router.get("/tg/{telegram_id}",tags=["Operations"])
def get_operations(telegram_id: int, db: Session = Depends(get_db)):
    return operation_crud.get_operations_by_telegram_id(db, telegram_id)

@router.get("/id/{operation_id}",tags=["Operations"])
def get_operations_by_id(operation_id: int, db: Session = Depends(get_db)):
    return operation_crud.get_operations_by_operation_id(db, operation_id)

@router.put("/{operation_id}", response_model=OperationUpdateSchema,tags=["Operations"])
def update_operation_endpoint(operation_id: int, data: OperationUpdateSchema, db: Session = Depends(get_db)):
    operation = operation_crud.update_operation(db, operation_id, data)
    if not operation:
        raise HTTPException(status_code=404, detail="Операция не найдена")
    return operation

@router.delete("/{operation_id}",tags=["Operations"])
def delete_operation(operation_id: int, db: Session = Depends(get_db)):
    return operation_crud.delete_operation(db, operation_id)

@router.get("/operations_date/{telegram_id}", response_model=List[OperationSchemaBase],tags=["Operations"])
def read_operations_by_date(
    telegram_id: int,
    start: datetime = Query(..., description="Start date in ISO format"),
    end: datetime = Query(..., description="End date in ISO format"),
    db: Session = Depends(get_db)
):
    print(start)
    print(end)
    return operation_crud.get_operations_by_date_range(db,telegram_id, start, end)
