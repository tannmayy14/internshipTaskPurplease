import React, { useState } from "react";
import { addProduct } from "../api";

function AddProduct() {
  const [product, setProduct] = useState({ name: "", price_per_unit: "", unit: "" });
  const [message, setMessage] = useState("");

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await addProduct(product);
      setMessage("Product added successfully!");
      setProduct({ name: "", price_per_unit: "", unit: "" });
    } catch (error) {
      setMessage(error.response?.data?.detail || "Error adding product");
    }
  };

  return (
    <div>
      <h2>Add Product</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Name"
          value={product.name}
          onChange={(e) => setProduct({ ...product, name: e.target.value })}
          required
        />
        <input
          type="number"
          placeholder="Price per unit"
          value={product.price_per_unit}
          onChange={(e) => setProduct({ ...product, price_per_unit: e.target.value })}
          required
        />
        <input
          type="text"
          placeholder="Unit"
          value={product.unit}
          onChange={(e) => setProduct({ ...product, unit: e.target.value })}
          required
        />
        <button type="submit">Add Product</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default AddProduct;