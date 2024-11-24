from sqlalchemy.orm import Session
from app.adapters.repositories.product_repository import ProductRepository

class RemoveProductUseCase:
    def __init__(self, repository: ProductRepository):
        self.repository = repository

    def execute(self, db: Session, product_id: str) -> bool:
        return self.repository.delete(db, product_id)
