from typing import Optional, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.adapters.repositories.product_repository import ProductRepository
from app.adapters.schemas.product_schemas import ProductResponseSchema, ProductUpdateSchema, ProductSaveSchema, \
    ProductSummary
from app.frameworks.database.database import get_db
from app.usecases.product.get_all_products import GetAllProductsUseCase
from app.usecases.product.get_product import GetProductUseCase
from app.usecases.product.get_summary import GetProductSummaryUseCase
from app.usecases.product.remove_product import RemoveProductUseCase
from app.usecases.product.save_product import SaveProductUseCase
from app.usecases.product.update_product import UpdateProductUseCase

router = APIRouter()
repository = ProductRepository()


@router.get("/stok/summary", response_model=List[ProductSummary])
def get_stock_sumary(db: Session = Depends(get_db)):
    use_case = GetProductSummaryUseCase(repository)
    return use_case.execute(db)


@router.get("/", response_model=List[ProductResponseSchema])
def get_products(name: Optional[str] = None, description: Optional[str] = None, db: Session = Depends(get_db)):
    use_case = GetAllProductsUseCase(repository)
    return use_case.execute(db, name, description)


@router.get("/{product_id}", response_model=ProductResponseSchema)
def get_product(product_id: str, db: Session = Depends(get_db)):
    use_case = GetProductUseCase(repository)
    product = use_case.execute(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.post("/", response_model=ProductResponseSchema)
def save_product(product_data: ProductSaveSchema, db: Session = Depends(get_db)):
    use_case = SaveProductUseCase(repository)
    return use_case.execute(db, product_data)


@router.put("/{product_id}", response_model=ProductResponseSchema)
def update_product(product_id: str, product_data: ProductUpdateSchema, db: Session = Depends(get_db)):
    use_case = UpdateProductUseCase(repository)
    updated_product = use_case.execute(db, product_id, product_data)
    if not updated_product:
        raise HTTPException(status_code=404, detail="Product not found")
    return updated_product


@router.delete("/{product_id}")
def delete_product(product_id: str, db: Session = Depends(get_db)):
    use_case = RemoveProductUseCase(repository)
    if not use_case.execute(db, product_id):
        raise HTTPException(status_code=404, detail="Product not found")
    return { "message": "Product deleted successfully" }
