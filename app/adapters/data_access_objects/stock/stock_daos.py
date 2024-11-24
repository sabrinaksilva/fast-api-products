from typing import List
from typing import Union
from uuid import UUID

from pydantic import BaseModel


class ProductStockSummaryDAO(BaseModel):
    product_id: UUID
    product_name: str
    product_unitary_value: float
    product_quantity: int
    total_value: Union[float, int]


class StockDAO(BaseModel):
    stock_summaries_daos: List[ProductStockSummaryDAO]
    total_value: Union[float, int]
    total_products: int
