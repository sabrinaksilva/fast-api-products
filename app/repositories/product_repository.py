from sqlalchemy.orm import Session
from app.entities.product import Product
from app.errors.exceptions.ProductNotFoundException import ProductNotFoundException

class ProductRepository:
    @staticmethod
    def get_all(db: Session):
        return db.query(Product).all()

    @staticmethod
    def get_by_id(db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if not product:
            raise ProductNotFoundException(product_id)
        return product

    @staticmethod
    def create(db: Session, product: Product):
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def update(db: Session, product_id: int, updated_data: dict):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            for key, value in updated_data.items():
                setattr(product, key, value)
            db.commit()
            db.refresh(product)
        return product

    @staticmethod
    def delete(db: Session, product_id: int):
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            db.delete(product)
            db.commit()
        return product
