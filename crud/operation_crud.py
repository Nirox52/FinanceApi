from sqlalchemy.orm import Session
from models.operation_schema import OperationSchemaBase,OperationUpdateSchema
from models.operations import Operations 
from datetime import datetime
from currency_parser import convert_to_usd

def create_operation(db: Session, telegram_id: int, type: str, amount: float, description: str):
    op_type = type.lower()
    operation = Operations(
        telegram_id=telegram_id,
        type=op_type,
        amount=amount,
        usd_amount = convert_to_usd(amount),
        description=description
    )
    db.add(operation)
    db.commit()
    db.refresh(operation)
    return operation

def get_operations_by_telegram_id(db: Session, telegram_id: int):
    return db.query(Operations).filter(Operations.telegram_id == telegram_id).all()

def get_operations_by_operation_id(db: Session, operation_id: int):
    return db.query(Operations).filter(Operations.operation_id == operation_id).all()

def delete_operation(db: Session, operation_id: int):
    operation = db.query(Operations).filter(Operations.operation_id == operation_id).first()
    if operation:
        db.delete(operation)
        db.commit()
        return True
    return False

def get_operations_by_date_range(db: Session,telegram_id:int, start_date: datetime, end_date: datetime):
    return (
        db.query(Operations)
        .filter(Operations.telegram_id == telegram_id)
        .filter(Operations.creareAt >= start_date)
        .filter(Operations.creareAt <= end_date)
        .all()
    )


def update_operation(db: Session, operation_id: int, data: OperationUpdateSchema):
    operation = db.query(Operations).get(operation_id)
    if not operation:
        return None
    
    if data.type is not None:
        operation.type = data.type
    if data.amount is not None:
        operation.amount = data.amount
    if data.description is not None:
        operation.description = data.description

    db.commit()
    db.refresh(operation)
    return operation

