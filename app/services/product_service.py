from sqlalchemy.orm import Session
from app.models.product import Product
from app.repositories.product_repository import ProductRepository

class ProductService:
    @staticmethod
    def get_all_products(db: Session):
        return ProductRepository.get_all(db)

    @staticmethod
    def get_product_by_id(db: Session, product_id: str):
        return ProductRepository.get_by_id(db, product_id)

    @staticmethod
    def create_product(db: Session, name: str, description: str, cost_price: float, selling_price: float):
        new_product = Product(name=name, description=description, cost_price=cost_price, selling_price=selling_price)
        return ProductRepository.create(db, new_product)

    @staticmethod
    def update_product(db: Session, product_id: str, updated_data: dict):
        return ProductRepository.update(db, product_id, updated_data)

    @staticmethod
    def delete_product(db: Session, product_id: str):
        return ProductRepository.delete(db, product_id)
