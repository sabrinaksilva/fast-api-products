from sqlalchemy.orm import Session
from typing import Optional
from app.domain.entities.product import Product
from app.adapters.repositories.product_repository import ProductRepository

class GetProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, db: Session, product_id: str) -> Optional[Product]:
        return self.repository.get_by_id(db, product_id)
