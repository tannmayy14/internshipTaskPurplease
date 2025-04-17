from fastapi import HTTPException
from typing import List, Dict
from models import Product, OrderItem


def validate_product_name_unique(name: str, products: List[Product]) -> None:
    """Validate that product name is unique"""
    for product in products:
        if product.name.lower() == name.lower():
            raise HTTPException(
                status_code=400,
                detail=f"Product with name '{name}' already exists"
            )


def validate_product_ids(items: List[OrderItem], products: Dict[int, Product]) -> None:
    """Validate that all product IDs in order items exist"""
    for item in items:
        if item.product_id not in products:
            raise HTTPException(
                status_code=400,
                detail=f"Product with ID {item.product_id} does not exist"
            )