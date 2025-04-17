from fastapi import APIRouter, Depends
from typing import List
from models import Product
from services.product_service import ProductService

router = APIRouter(tags=["Products"])


def get_product_service():
    return ProductService()


@router.post("/products", response_model=Product, status_code=201)
def add_product(product: Product, product_service: ProductService = Depends(get_product_service)):
    """Add a new product"""
    return product_service.add_product(product)


@router.get("/products", response_model=List[Product])
def get_products(product_service: ProductService = Depends(get_product_service)):
    """Get all products"""
    return product_service.get_all_products()