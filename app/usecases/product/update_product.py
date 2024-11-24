from sqlalchemy.orm import Session
from typing import Optional
from app.adapters.repositories.product_repository import ProductRepository
from app.adapters.schemas.product_schemas import ProductUpdateSchema

class UpdateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, db: Session, product_id: str, product_data: ProductUpdateSchema) -> Optional[Product]:
        return self.repository.update(db, product_id, product_data.dict(exclude_unset=True))
