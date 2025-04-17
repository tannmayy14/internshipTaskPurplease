import pytest
from services.order_service import OrderService
from services.product_service import ProductService
from models import Order, OrderItem, Product
from fastapi import HTTPException

def test_create_order():
    # Set load_from_file=False to avoid loading existing products from json file which interferes with the test
    product_service = ProductService(load_from_file=False)
    order_service = OrderService(product_service)
    
    # Add products
    product1 = product_service.add_product(Product(name="Wheat", price_per_unit=50, unit="kg"))
    product2 = product_service.add_product(Product(name="Rice", price_per_unit=60, unit="kg"))
    
    # Create order
    order = Order(
        customer_name="Tanmay",
        items=[
            OrderItem(product_id=product1.id, quantity=2),
            OrderItem(product_id=product2.id, quantity=1)
        ]
    )
    created_order = order_service.create_order(order)
    
    # Verify the order ID is assigned correctly
    assert created_order.order_id is not None  # Ensure the order ID is not None
    assert created_order.customer_name == "Tanmay"
    assert len(created_order.items) == 2
    assert created_order.total_amount == 160

def test_create_order_with_invalid_product_id():
    product_service = ProductService(load_from_file=False)
    order_service = OrderService(product_service)
    
    # Create order with an invalid product ID
    order = Order(
        customer_name="Tanmay",
        items=[
            OrderItem(product_id=999, quantity=2)
        ]
    )
    
    # Now we expect an HTTPException rather than a generic Exception
    with pytest.raises(HTTPException) as exc_info:
        order_service.create_order(order)
    
    assert exc_info.value.status_code == 400
    assert "Product with ID 999 does not exist" in exc_info.value.detail