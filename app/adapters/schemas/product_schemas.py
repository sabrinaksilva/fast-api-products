from typing import Optional
from typing import Union
from uuid import UUID

from pydantic import BaseModel, Field


class ProductSummary(BaseModel):
    id: UUID
    name: str
    total_value: Union[float, int]


class ProductBaseSchema(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = Field(None, max_length=300)
    price: float = Field(..., ge=0)
    quantity: int = Field(..., ge=0)


class ProductSaveSchema(ProductBaseSchema):
    pass


class ProductUpdateSchema(ProductBaseSchema):
    pass


class ProductResponseSchema(BaseModel):
    id: UUID
    name: str
    description: str
    price: float
    quantity: int

    class Config:
        orm_mode = True
