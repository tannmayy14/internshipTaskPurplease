import json
from typing import Dict, List
from models import Order, OrderResponse, OrderItemResponse
from services.product_service import ProductService
from utils.validators import validate_product_ids
ORDERS_FILE = "orders.json"


class OrderService:
    def __init__(self, product_service: ProductService,load_from_file=True):
        self.orders: Dict[int, OrderResponse] = {}
        self.next_id = 101
        self.product_service = product_service
        if load_from_file:
            self.load_orders()

    def create_order(self, order: Order) -> OrderResponse:
        """Create a new order"""
        validate_product_ids(order.items, self.product_service.products)
        
        # Calculate prices and create response items
        response_items = []
        total_amount = 0.0
        
        for item in order.items:
            product = self.product_service.get_product_by_id(item.product_id)
            item_price = product.price_per_unit * item.quantity
            total_amount += item_price
            
            response_items.append(OrderItemResponse(
                product_id=item.product_id,
                product_name=product.name,
                quantity=item.quantity,
                price=item_price
            ))
        
        # Create order response
        order_response = OrderResponse(
            order_id=self.next_id,
            customer_name=order.customer_name,
            items=response_items,
            total_amount=total_amount
        )
        
        
        self.orders[self.next_id] = order_response
        self.next_id += 1
        # Save order to a json file
        self.save_orders()
        
        return order_response

    def get_all_orders(self) -> List[OrderResponse]:
        """Get all orders"""
        return list(self.orders.values())
    
    def load_orders(self):
        """Load orders from the JSON file."""
        try:
            with open(ORDERS_FILE, "r") as file:
                data = json.load(file)
                self.orders = {int(k): OrderResponse(**v) for k, v in data.items()}
                if self.orders:
                    self.next_id = max(self.orders.keys()) + 1
        except FileNotFoundError:
            self.orders = {}

    def save_orders(self):
        """Save orders to the JSON file."""
        with open(ORDERS_FILE, "w") as file:
            json.dump({k: v.model_dump() for k, v in self.orders.items()}, file)