from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from app.config.database import Base, engine, SessionLocal
from app.services.product_service import ProductService
from app.errors.exceptions.ProductNotFoundException import ProductNotFoundException
from app.errors.handlers.not_found_handlers import product_not_found_exception_handler

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
