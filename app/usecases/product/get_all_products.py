from typing import List, Optional

from sqlalchemy.orm import Session

from app.adapters.repositories.product_repository import ProductRepository
from app.adapters.schemas.product_schemas import ProductResponseSchema


class GetAllProductsUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, db: Session, name: Optional[str] = None, description: Optional[str] = None) -> List[
        ProductResponseSchema]:
        products = self.repository.get_all(db, name, description)
        if (products):
            print(len(products))

        return [ProductResponseSchema.from_orm(product) for product in products]
