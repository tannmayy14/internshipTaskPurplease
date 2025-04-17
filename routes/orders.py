from fastapi import APIRouter,Depends
from typing import List
from models import Order, OrderResponse
from services.product_service import ProductService
from services.order_service import OrderService

router = APIRouter(tags=["Orders"])


def get_product_service():
    return ProductService()


def get_order_service(product_service: ProductService = Depends(get_product_service)):
    return OrderService(product_service)


@router.post("/orders", response_model=OrderResponse, status_code=201)
def create_order(order: Order, order_service: OrderService = Depends(get_order_service)):
    """Create a new order"""
    return order_service.create_order(order)


@router.get("/orders", response_model=List[OrderResponse])
def get_orders(order_service: OrderService = Depends(get_order_service)):
    """Get all orders"""
    return order_service.get_all_orders()