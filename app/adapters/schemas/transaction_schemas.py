from pydantic import BaseModel, Field
from uuid import UUID
from datetime import date
from enum import Enum

class TransactionType(str, Enum):
    IN = "in"
    OUT = "out"

class TransactionBase(BaseModel):
    date: date
    productId: str
    type: TransactionType
    productQuantity: int = Field(gt=0)
    totalValue: float

class TransactionCreate(TransactionBase):
    pass

class Transaction(TransactionBase):
    id: UUID

    class Config:
        orm_mode = True
