from sqlalchemy import Table, Column, Integer,Float, String, MetaData,ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column
from database import Base
import enum
import datetime


class operation_type(enum.Enum):
    income = "Income"
    expence = "Expence"

class Operations(Base):
    __tablename__="operations"

    operation_id: Mapped[int] = mapped_column(primary_key=True)
    telegram_id:Mapped[int] = mapped_column(ForeignKey("users.telegram_id",ondelete="CASCADE"))
    type: Mapped[operation_type]
    amount:Mapped[float]
    description:Mapped[str]
    creareAt:Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc',now())"))
    updateAt:Mapped[datetime.datetime] = mapped_column(server_default=text("TIMEZONE('utc',now())"),onupdate=datetime.datetime.utcnow)



