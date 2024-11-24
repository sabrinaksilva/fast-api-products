from fastapi import FastAPI

from app.frameworks.api.product_routes import router as product_router
from app.frameworks.database.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(product_router, prefix="/products", tags=["Products"])
