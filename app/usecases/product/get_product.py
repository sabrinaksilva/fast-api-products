from typing import Optional

from sqlalchemy.orm import Session

from app.adapters.repositories.product_repository import ProductRepository
from app.adapters.schemas.product_schemas import ProductResponseSchema


class GetProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, db: Session, product_id: str) -> Optional[ProductResponseSchema]:
        product = self.repository.get_by_id(db, product_id)
        if product:
            return ProductResponseSchema.from_orm(product)
        return None
