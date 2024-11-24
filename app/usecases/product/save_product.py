from sqlalchemy.orm import Session

from app.adapters.repositories.product_repository import ProductRepository
from app.adapters.schemas.product_schemas import ProductSaveSchema, ProductResponseSchema
from app.domain.entities.product import Product


class SaveProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, db: Session, product_data: ProductSaveSchema) -> ProductResponseSchema:
        new_product = Product(**product_data.dict())
        saved_product = self.repository.create(db, new_product)
        return ProductResponseSchema.from_orm(saved_product)
