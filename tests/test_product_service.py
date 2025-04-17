import pytest
from services.product_service import ProductService
from models import Product
from fastapi import HTTPException

def test_add_product():
    # Set load_from_file=False to avoid loading existing products from json file which interferes with the test
    product_service = ProductService(load_from_file=False)
    product = Product(name="Wheat", price_per_unit=50, unit="kg")
    
    # Add product
    added_product = product_service.add_product(product)
    
    assert added_product.id == 1
    assert added_product.name == "Wheat"
    assert added_product.price_per_unit == 50
    assert added_product.unit == "kg"

def test_add_duplicate_product():
    product_service = ProductService(load_from_file=False)
    product1 = Product(name="Wheat", price_per_unit=50, unit="kg")
    product2 = Product(name="Wheat", price_per_unit=60, unit="kg")
    
    # Add first product
    product_service.add_product(product1)
    
    # Adding duplicate product should raise an exception
    with pytest.raises(HTTPException) as exc_info:
        product_service.add_product(product2)
    
    assert exc_info.value.status_code == 400
    assert "Product with name 'Wheat' already exists" in exc_info.value.detail

def test_get_all_products():
    product_service = ProductService(load_from_file=False)
    product1 = Product(name="Sugar", price_per_unit=50, unit="kg")
    product2 = Product(name="Rice", price_per_unit=60, unit="kg")
    
    # Add products
    product_service.add_product(product1)
    product_service.add_product(product2)
    
    products = product_service.get_all_products()
    assert len(products) == 2
    
    # Sort products by name for consistent testing
    products_sorted = sorted(products, key=lambda p: p.name)
    assert products_sorted[0].name == "Rice"
    assert products_sorted[1].name == "Sugar"

def test_get_product_by_id():
    product_service = ProductService(load_from_file=False)
    product = Product(name="Wheat", price_per_unit=50, unit="kg")
    
    # Add product
    added_product = product_service.add_product(product)
    
    # Get product by ID
    fetched_product = product_service.get_product_by_id(added_product.id)
    assert fetched_product.name == "Wheat"

def test_get_product_by_invalid_id():
    product_service = ProductService(load_from_file=False)
    
    # Fetching a product with an invalid ID should raise an exception
    with pytest.raises(HTTPException) as exc_info:
        product_service.get_product_by_id(999)
    
    assert exc_info.value.status_code == 404
    assert "Product with ID 999 not found" in exc_info.value.detail