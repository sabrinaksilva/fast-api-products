from typing import Union, List
from uuid import UUID

from pydantic import BaseModel

from app.adapters.data_access_objects.stock.stock_daos import ProductStockSummaryDAO, StockDAO


class StockSummaryResponse(BaseModel):
    productId: UUID
    productName: str
    productPrice: float
    productQuantity: int
    totalValue: Union[float, int]


    @classmethod
    def from_dao(cls, dao: "ProductStockSummaryDAO") -> "StockSummaryResponse":
        return cls(productId=dao.product_id, productName=dao.product_name, productPrice=dao.product_unitary_value,
                   productQuantity=dao.product_quantity, totalValue=dao.total_value, )


class StockResponse(BaseModel):
    summaries: List[StockSummaryResponse]
    totalValue: Union[float, int]
    totalProducts: int


    @classmethod
    def from_dao(cls, dao: StockDAO) -> "StockResponse":
        return cls(summaries=[StockSummaryResponse.from_dao(summary) for summary in dao.stock_summaries_daos],
                   totalValue=dao.total_value, totalProducts=dao.total_products, )
