from fastapi import Request
from fastapi.responses import JSONResponse
from app.errors.exceptions.ProductNotFoundException import ProductNotFoundException

def product_not_found_exception_handler(request: Request, exc: ProductNotFoundException):
    return JSONResponse(
        status_code=404,
        content={"code": "PRODUCT_NOT_FOUND"}
    )
