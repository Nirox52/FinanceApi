from sqlalchemy import Table, Column, Integer,Float, String, MetaData,ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class Users(Base):
    __tablename__="users"

    user_id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id:Mapped[int] = mapped_column(unique=True)

