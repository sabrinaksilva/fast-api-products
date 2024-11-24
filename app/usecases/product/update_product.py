from typing import Optional

from sqlalchemy.orm import Session

from app.adapters.repositories.product_repository import ProductRepository
from app.adapters.schemas.product_schemas import ProductResponseSchema, ProductUpdateSchema


class UpdateProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, db: Session, product_id: str, product_data: ProductUpdateSchema) -> Optional[
        ProductResponseSchema]:
        updated_product = self.repository.update(db, product_id, product_data.dict(exclude_unset=True))
        if updated_product:
            return ProductResponseSchema.from_orm(updated_product)
        return None
