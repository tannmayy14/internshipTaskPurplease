from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import products, orders
from services.product_service import ProductService
from services.order_service import OrderService

app = FastAPI(
    title="Smart Grocery Order API",
    description="A RESTful API for a basic grocery ordering system",
    version="1.0.0"
)

# Creating singular instances of services
product_service = ProductService()
order_service = OrderService(product_service)


def get_product_service():
    return product_service


def get_order_service():
    return order_service


# Override in routes
products.get_product_service = get_product_service
orders.get_product_service = get_product_service
orders.get_order_service = get_order_service

# Include routers
app.include_router(products.router)
app.include_router(orders.router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (or specify your frontend URL)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Smart Grocery Order API"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)