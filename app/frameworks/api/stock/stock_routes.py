from typing import List, Optional
from uuid import UUID

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.adapters.repositories.stock_repository import StockRepository
from app.adapters.schemas.stock_schemas import StockResponse
from app.adapters.schemas.stock_schemas import StockSummaryResponse
from app.frameworks.database.database import get_db
from app.usecases.stock.get_full_stock import GetFullStockUseCase
from app.usecases.stock.get_stock_summary import GetProductsStockSummaryUseCase


router = APIRouter()
repository = StockRepository()


@router.get("/", response_model=StockResponse)
def get_full_stock(db: Session = Depends(get_db), product_ids: Optional[List[str]] = Query(None)):
    use_case = GetFullStockUseCase(repository)
    product_ids_uuid = [UUID(product_id) for product_id in product_ids] if product_ids else None
    return use_case.execute(db, product_ids=product_ids_uuid)


@router.get("/summary", response_model=List[StockSummaryResponse])
def get_stocks_summary(db: Session = Depends(get_db)):
    use_case = GetProductsStockSummaryUseCase(repository)
    return use_case.execute(db)
