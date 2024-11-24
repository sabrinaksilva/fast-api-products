from typing import List

from sqlalchemy.orm import Session

from app.adapters.repositories.stock_repository import StockRepository
from app.adapters.schemas.stock_schemas import ProductStockSummaryDAO, StockSummaryResponse


class GetProductsStockSummaryUseCase:

    def __init__(self, repository: StockRepository) -> None:
        self.repository = repository


    def execute(self, session: Session) -> List[StockSummaryResponse]:
        dao: List[ProductStockSummaryDAO] = self.repository.get_summary(session)
        return [StockSummaryResponse.from_dao(d) for d in dao]
