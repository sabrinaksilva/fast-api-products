from datetime import date
from typing import List, Optional

from sqlalchemy.orm import Session

from app.adapters.schemas.transaction_schemas import TransactionCreate, TransactionType


class TransactionRepository:
    @staticmethod
    def create_transaction(db: Session, transaction: TransactionCreate) -> Transaction:
        db_transaction = Transaction(**transaction.dict())
        db.add(db_transaction)
        db.commit()
        db.refresh(db_transaction)
        return db_transaction

    @staticmethod
    def get_transaction_by_id(db: Session, transaction_id: str) -> Optional[Transaction]:
        return db.query(Transaction).filter(Transaction.id == transaction_id).first()

    @staticmethod
    def get_all_transactions(db: Session, start_date: Optional[date] = None, end_date: Optional[date] = None,
            product_id: Optional[str] = None, transaction_type: Optional[TransactionType] = None, ) -> List[
        Transaction]:
        query = db.query(Transaction)
        if start_date:
            query = query.filter(Transaction.date >= start_date)
        if end_date:
            query = query.filter(Transaction.date <= end_date)
        if product_id:
            query = query.filter(Transaction.productId == product_id)
        if transaction_type:
            query = query.filter(Transaction.type == transaction_type)
        return query.all()
