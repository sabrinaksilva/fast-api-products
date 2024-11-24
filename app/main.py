from datetime import date
from typing import Optional, List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import Base, engine, SessionLocal
from app.schemas.transaction_schemas import Transaction, TransactionCreate, TransactionType
from app.services.product_service import ProductService
from app.errors.exceptions.ProductNotFoundException import ProductNotFoundException
from app.errors.handlers.not_found_handlers import product_not_found_exception_handler
from app.services.transaction_service import TransactionService

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_exception_handler(ProductNotFoundException, product_not_found_exception_handler)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products")
def list_products(db: Session = Depends(get_db)):
    return ProductService.get_all_products(db)

@app.get("/products/{product_id}")
def get_product(product_id: str, db: Session = Depends(get_db)):
    return ProductService.get_product_by_id(db, product_id)

@app.post("/products")
def create_product(name: str, description: str = None, cost_price: float = 0.0, selling_price: float = 0.0, db: Session = Depends(get_db)):
    return ProductService.create_product(db, name, description, cost_price, selling_price)

@app.put("/products/{product_id}")
def update_product(product_id: str, updated_data: dict, db: Session = Depends(get_db)):
    return ProductService.update_product(db, product_id, updated_data)

@app.delete("/products/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    return ProductService.delete_product(db, product_id)

@app.post("/transactions/", response_model=Transaction)
def create_transaction(transaction: TransactionCreate, db: Session = Depends(get_db)):
    return TransactionService.create_transaction(db, transaction)

@app.get("/transactions/{transaction_id}", response_model=Transaction)
def get_transaction(transaction_id: str, db: Session = Depends(get_db)):
    transaction = TransactionService.get_transaction_by_id(db, transaction_id)
    if not transaction:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return transaction

@app.get("/transactions/", response_model=List[Transaction])
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