from sqlalchemy import Column, Integer, String, Float
from app.config.database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True, nullable=False)
    description = Column(String, nullable=True)
    value = Column(Float, nullable=False)
