from pydantic import BaseModel, Field, validator
from typing import Optional
from uuid import UUID

class ProductBaseSchema(BaseModel):
    name: str = Field(..., min_length=1)
    description: Optional[str] = Field(None, max_length=300)
    cost_price: Optional[float] = Field(None, ge=0)
    selling_price: float = Field(..., gt=0)

    @validator("selling_price")
    def validate_prices(cls, value, values):
        cost_price = values.get("cost_price", 0)
        if value < cost_price:
            raise ValueError("selling_price must be greater than or equal to cost_price")
        return round(value, 2)

class ProductSaveSchema(ProductBaseSchema):
    @validator("cost_price", pre=True, always=True)
    def default_cost_price(cls, value):
        return round(value or 0.0, 2)

class ProductUpdateSchema(ProductBaseSchema):
    pass

class ProductResponseSchema(ProductBaseSchema):
    id: UUID

    class Config:
        orm_mode = True
