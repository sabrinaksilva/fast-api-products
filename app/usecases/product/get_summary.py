from sqlalchemy.orm import Session

from app.adapters.repositories.product_repository import ProductRepository
from app.adapters.schemas.product_schemas import ProductSummary


class GetProductSummaryUseCase:
    def __init__(self, repository: ProductRepository) -> None:
        self.repository = repository

    def execute(self, session: Session) -> list[ProductSummary]:
        return self.repository.get_summary(session);
