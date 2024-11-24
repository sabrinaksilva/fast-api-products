from sqlalchemy.orm import Session
from typing import List, Optional
from datetime import date

from app.models.transaction import Transaction
from app.repositories.transaction_repository import TransactionRepository
from app.schemas.transaction_schemas import TransactionCreate, TransactionType


class TransactionService:
    @staticmethod
    def create_transaction(db: Session, transaction: TransactionCreate) -> Transaction:
        return TransactionRepository.create_transaction(db, transaction)

    @staticmethod
    def get_transaction_by_id(db: Session, transaction_id: str) -> Optional[Transaction]:
        return TransactionRepository.get_transaction_by_id(db, transaction_id)

    @staticmethod
    def get_all_transactions(
        db: Session,
        start_date: Optional[date] = None,
        end_date: Optional[date] = None,
        product_id: Optional[str] = None,
        transaction_type: Optional[TransactionType] = None,
    ) -> List[Transaction]:
        return TransactionRepository.get_all_transactions(
            db, start_date, end_date, product_id, transaction_type
        )
