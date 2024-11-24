from typing import Optional, List
from uuid import UUID

from sqlalchemy.orm import Session

from app.adapters.repositories.stock_repository import StockRepository
from app.adapters.schemas.stock_schemas import StockResponse


class GetFullStockUseCase:

    def __init__(self, repository: StockRepository) -> None:
        self.repository = repository


    def execute(self, db: Session, product_ids: Optional[List[UUID]] = None) -> StockResponse:
        stock_dao = self.repository.get_full_stock(db, product_ids)
        return StockResponse.from_dao(stock_dao)
