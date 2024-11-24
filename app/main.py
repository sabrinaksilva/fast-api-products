from datetime import date
from typing import Optional, List
from fastapi import APIRouter, Depends, HTTPException, FastAPI
from sqlalchemy.orm import Session
from app.config.database import Base, engine, SessionLocal
from app.schemas.product_schemas import ProductResponseSchema, ProductUpdateSchema, ProductSaveSchema
from app.schemas.transaction_schemas import Transaction, TransactionCreate, TransactionType
from app.services.product_service import ProductService
from app.services.transaction_service import TransactionService

Base.metadata.create_all(bind=engine)
app = FastAPI()
router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/products/", response_model=List[ProductResponseSchema])
def get_products(
    name: Optional[str] = None,
    description: Optional[str] = None,
    db: Session = Depends(get_db),
):
    return ProductService.get_all_products(db, name, description)

@router.get("/products/{product_id}", response_model=ProductResponseSchema)
def get_product(product_id: str, db: Session = Depends(get_db)):
    product = ProductService.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products/", response_model=ProductResponseSchema)
def save_product(product_data: ProductSaveSchema, db: Session = Depends(get_db)):
    return ProductService.save_product(db, product_data)

@router.put("/products/{product_id}", response_model=ProductResponseSchema)
def update_product(product_id: str, product_data: ProductUpdateSchema, db: Session = Depends(get_db)):
    updated_product = ProductService.update_product(db, product_id, product_data)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product

@router.delete("/products/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    if not ProductService.delete_product(db, product_id):
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}


@router.post("/transactions/", response_model=Transaction)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return TransactionService.create_transaction(db, transaction)

@router.get("/transactions/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: str, db: Session = Depends(get_db)):
    transaction = TransactionService.get_transaction_by_id(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@router.get("/transactions/", response_model=List[Transaction])
def get_all_transactions(
    start_date: Optional[date] = None,
    end_date: Optional[date] = None,
    product_id: Optional[str] = None,
    transaction_type: Optional[TransactionType] = None,
    db: Session = Depends(get_db),
):
    return TransactionService.get_all_transactions(
        db, start_date, end_date, product_id, transaction_type
    )

