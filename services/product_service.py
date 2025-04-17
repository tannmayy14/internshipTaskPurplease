import json
from fastapi import APIRouter, HTTPException, Depends
from typing import List, Dict
from models import Product
from utils.validators import validate_product_name_unique
router = APIRouter(tags=["Orders"])
PRODUCTS_FILE = "products.json"

class ProductService:
    def __init__(self, load_from_file: bool = True):
        self.products: Dict[int, Product]={}
        self.next_id = 1
        if load_from_file:
            self.load_products()
    def add_product(self, product: Product) -> Product:
        """Add a new product"""
        validate_product_name_unique(product.name, list(self.products.values()))
        product.id = self.next_id
        self.products[self.next_id] = product
        self.next_id += 1
        self.save_products()
        return product

    def get_all_products(self) -> List[Product]:
        """Get all products"""
        return list(self.products.values())
    
    def get_product_by_id(self, product_id: int) -> Product:
        """Get a product by its ID"""
        product = self.products.get(product_id)
        if not product:
            raise HTTPException(status_code=404, detail=f"Product with ID {product_id} not found")
        return product
    def load_products(self):
        """Load products from the JSON file."""
        try:
            with open(PRODUCTS_FILE, "r") as file:
                data = json.load(file)
                self.products = {int(k): Product(**v) for k, v in data.items()}
                if self.products:
                    self.next_id = max(self.products.keys()) + 1
        except FileNotFoundError:
            self.products = {}
    def save_products(self):
        """Save products to the JSON file."""
        with open(PRODUCTS_FILE, "w") as file:
            json.dump({k: v.model_dump() for k, v in self.products.items()}, file)


def get_product_service():
    return ProductService()
