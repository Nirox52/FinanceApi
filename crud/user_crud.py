from sqlalchemy.orm import Session
from models.users import Users

def create_user(db: Session, telegram_id: int):
    user = Users(telegram_id=telegram_id)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_by_telegram_id(db: Session, telegram_id: int):
    return db.query(Users).filter(Users.telegram_id == telegram_id).first()

def delete_user_by_telegram_id(db: Session, telegram_id: int):
    user = db.query(Users).filter(Users.telegram_id == telegram_id).first()
    if user:
        db.delete(user)
        db.commit()
        return True
    return False

