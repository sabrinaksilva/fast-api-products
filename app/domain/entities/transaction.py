from sqlalchemy import Column, String, Integer, Float, Date, Enum
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum

from app.frameworks.database.database import Base


class TransactionType(str, enum.Enum):
    IN = "in"
    OUT = "out"

class Transaction(Base):
    __tablename__ = "transactions"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    date = Column(Date, nullable=False)
    productId = Column(String, nullable=False)
    type = Column(Enum(TransactionType), nullable=False)
    productQuantity = Column(Integer, nullable=False)
    totalValue = Column(Float, nullable=False)
