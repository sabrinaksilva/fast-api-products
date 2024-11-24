from typing import List, Optional
from uuid import UUID

from sqlalchemy.orm import Session
from sqlalchemy.sql import func, label

from app.adapters.data_access_objects.stock.stock_daos import ProductStockSummaryDAO, StockDAO
from app.domain.entities.product import Product


class StockRepository:

    @staticmethod
    def get_summary(db: Session) -> List[ProductStockSummaryDAO]:
        query = db.query(Product.id, Product.name, Product.price, Product.quantity,
            label("total_value", Product.price * Product.quantity))

        return [ProductStockSummaryDAO(product_id=prod.id, product_name=prod.name, product_unitary_value=prod.price,
            product_quantity=prod.quantity, total_value=prod.total_value) for prod in query.all()]


    @staticmethod
    def get_full_stock(db: Session, product_ids: Optional[List[UUID]] = None) -> StockDAO:
        summaries_query = db.query(Product.id, Product.name, Product.price, Product.quantity,
            label("total_value", Product.price * Product.quantity))
        if product_ids:
            summaries_query = summaries_query.filter(Product.id.in_(product_ids))

        stock_summaries = [
            ProductStockSummaryDAO(product_id=prod.id, product_name=prod.name, product_unitary_value=prod.price,
                product_quantity=prod.quantity, total_value=prod.total_value) for prod in summaries_query.all()]

        totals_query = db.query(func.sum(Product.price * Product.quantity).label("total_value"),
            func.sum(Product.quantity).label("total_products")).one()

        total_value = totals_query.total_value or 0
        total_products = totals_query.total_products or 0

        return StockDAO(stock_summaries_daos=stock_summaries, total_value=total_value, total_products=total_products)
