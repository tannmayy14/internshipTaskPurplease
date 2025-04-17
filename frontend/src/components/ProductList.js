import React, { useEffect, useState } from "react";
import { getProducts } from "../api";

function ProductList() {
  const [products, setProducts] = useState([]);

  const fetchProducts = async () => {
    try {
      const response = await getProducts();
      setProducts(response.data);
    } catch (error) {
      console.error("Error fetching products:", error);
    }
  };

  useEffect(() => {
    fetchProducts();
  }, []);

  return (
    <div>
      <h2>Product List</h2>
      <ul>
        {products.map((product) => (
          <li key={product.id}>
            {product.name} - Rs.{product.price_per_unit} Count:{product.unit}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductList;