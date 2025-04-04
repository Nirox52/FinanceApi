from sqlalchemy.orm import Session
from models.operations import Operations, operation_type

def create_operation(db: Session, telegram_id: int, type: str, amount: float, description: str):
    op_type = operation_type[type.lower()]
    operation = Operations(
        telegram_id=telegram_id,
        type=op_type,
        amount=amount,
        description=description
    )
    db.add(operation)
    db.commit()
    db.refresh(operation)
    return operation

def get_operations_by_telegram_id(db: Session, telegram_id: int):
    return db.query(Operations).filter(Operations.telegram_id == telegram_id).all()

def delete_operation(db: Session, operation_id: int):
    operation = db.query(Operations).filter(Operations.operation_id == operation_id).first()
    if operation:
        db.delete(operation)
        db.commit()
        return True
    return False

