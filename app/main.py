from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app.config.database import Base, engine, SessionLocal
from app.services.product_service import ProductService

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/products")
def get_products(db: Session = Depends(get_db)):
    return ProductService.get_all_products(db)

@app.get("/products/{product_id}")
def get_product(product_id: int, db: Session = Depends(get_db)):
    product = ProductService.get_product_by_id(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products")
def create_product(name: str, description: str = None, value: float = 0.0, db: Session = Depends(get_db)):
    return ProductService.create_product(db, name, description, value)

@app.put("/products/{product_id}")
def update_product(product_id: int, updated_data: dict, db: Session = Depends(get_db)):
    product = ProductService.update_product(db, product_id, updated_data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):
    product = ProductService.delete_product(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"detail": "Product deleted successfully"}
