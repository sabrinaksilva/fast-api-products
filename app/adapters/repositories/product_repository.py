from typing import List, Optional

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.domain.entities.product import Product


class ProductRepository:

    @staticmethod
    def get_all(db: Session, name: Optional[str] = None, description: Optional[str] = None) -> List[Product]:
        query = db.query(Product)
        if name or description:
            query = query.filter(or_(Product.name.ilike(f"%{name}%"), Product.description.ilike(f"%{description}%")))
        return query.all()

    @staticmethod
    def get_by_id(db: Session, product_id: str) -> Optional[Product]:
        return db.query(Product).filter(Product.id == product_id).first()

    @staticmethod
    def create(db: Session, product: Product) -> Product:
        db.add(product)
        db.commit()
        db.refresh(product)
        return product

    @staticmethod
    def update(db: Session, product_id: str, updated_data: dict) -> Optional[Product]:
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            for key, value in updated_data.items():
                setattr(product, key, value)
            db.commit()
            db.refresh(product)
            return product
        return None

    @staticmethod
    def delete(db: Session, product_id: str) -> bool:
        product = db.query(Product).filter(Product.id == product_id).first()
        if product:
            db.delete(product)
            db.commit()
            return True
        return False
