from sqlalchemy.orm import Session
from app.models.product import Product
from app.repositories.product_repository import ProductRepository
from typing import List, Optional

from app.schemas.product_schemas import ProductSaveSchema, ProductUpdateSchema


class ProductService:
    @staticmethod
    def get_all_products(db: Session, name: Optional[str] = None, description: Optional[str] = None) -> List[Product]:
        return ProductRepository.get_all(db, name, description)

    @staticmethod
    def get_product_by_id(db: Session, product_id: str) -> Optional[Product]:
        return ProductRepository.get_by_id(db, product_id)

    @staticmethod
    def save_product(db: Session, product_data: ProductSaveSchema) -> Product:
        new_product = Product(**product_data.dict())
        return ProductRepository.create(db, new_product)

    @staticmethod
    def update_product(db: Session, product_id: str, product_data: ProductUpdateSchema) -> Optional[Product]:
        return ProductRepository.update(db, product_id, product_data.dict(exclude_unset=True))

    @staticmethod
    def delete_product(db: Session, product_id: str) -> bool:
        return ProductRepository.delete(db, product_id)
