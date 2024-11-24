from sqlalchemy.orm import Session
from typing import List, Optional
from app.domain.entities.product import Product
from app.adapters.repositories.product_repository import ProductRepository

class GetAllProductsUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, db: Session, name: Optional[str] = None, description: Optional[str] = None) -> List[Product]:
        return self.repository.get_all(db, name, description)
