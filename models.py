from pydantic import BaseModel, ConfigDict, Field
from typing import List, Optional


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price_per_unit: float = Field(gt=0)
    unit: str

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "name": "Wheat",
                "price_per_unit": 50,
                "unit": "kg"
            },
            "description": "Represents a product with a name, price per unit, and unit of measurement."
        }
    )


class OrderItem(BaseModel):
    product_id: int
    quantity: int = Field(gt=0)
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "product_id": 1,
                "quantity": 2
            },
            "description": "Represents an item in an order with a product ID and quantity."
        }
   )

class Order(BaseModel):
    customer_name: str
    items: List[OrderItem]

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "customer_name": "Ravi",
                "items": [
                    {"product_id": 1, "quantity": 2},
                    {"product_id": 2, "quantity": 1}
                ]
            },
            "description": "Represents an order with a customer name and a list of items of their order."
        }
    )


class OrderItemResponse(BaseModel):
    product_id: int
    product_name: str
    quantity: int
    price: float


class OrderResponse(BaseModel):
    order_id: int
    customer_name: str
    items: List[OrderItemResponse]
    total_amount: float

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "order_id": 101,
                "customer_name": "Ravi",
                "items": [
                    {"product_id": 1, "product_name": "Wheat", "quantity": 2, "price": 100},
                    {"product_id": 2, "product_name": "Rice", "quantity": 1, "price": 60}
                ],
                "total_amount": 160
            },
            "description": "Represents the response for an order with details including order ID, customer name, items, and total amount."
        }
    )