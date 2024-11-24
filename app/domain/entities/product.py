import uuid

from sqlalchemy import Column, String, Float, Integer, CheckConstraint
from sqlalchemy.dialects.postgresql import UUID

from app.frameworks.database.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True, index=True, nullable=False)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Float, nullable=False, default=0.0)
    quantity = Column(Integer, nullable=False, default=0)

    __table_args__ = (CheckConstraint('quantity >= 0', name='check_quantity_non_negative'),)
