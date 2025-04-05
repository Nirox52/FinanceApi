from pydantic import BaseModel
from typing import Optional


class OperationSchemaBase(BaseModel):
    telegram_id: int
    type: str
    amount: float
    usd_amount:float
    description: str

class OperationCreateSchema(BaseModel):
    telegram_id: int
    type: str
    amount: float
    description: str

class OperationUpdateSchema(BaseModel):
    type: Optional[str]
    amount: Optional[float]
    description: Optional[str]
    


class OperationShema(OperationSchemaBase):
    operation_id: int

