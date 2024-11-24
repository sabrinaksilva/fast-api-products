from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.frameworks.api.product_routes import router as product_router
from app.frameworks.database.database import Base, engine

app = FastAPI()
app.add_middleware(CORSMiddleware, allow_origins=["*"],  # Permite todas as origens (inseguro em produção)
                   allow_credentials=True, allow_methods=["*"],  # Permite todos os métodos HTTP
                   allow_headers=["*"],  # Permite todos os cabeçalhos
                   )
Base.metadata.create_all(bind=engine)
app.include_router(product_router, prefix="/products", tags=["Products"])
