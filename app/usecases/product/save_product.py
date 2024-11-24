from sqlalchemy.orm import Session
from app.domain.entities.product import Product
from app.adapters.repositories.product_repository import ProductRepository
from app.adapters.schemas.product_schemas import ProductSaveSchema

class SaveProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, db: Session, product_data: ProductSaveSchema) -> Product:
        new_product = Product(**product_data.dict())
        return self.repository.create(db, new_product)
