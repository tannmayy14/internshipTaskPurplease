import React, { useState, useEffect } from "react";
import { getProducts, placeOrder } from "../api";

function PlaceOrder() {
  const [products, setProducts] = useState([]);
  const [order, setOrder] = useState({ customer_name: "", items: [] });
  const [message, setMessage] = useState("");

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const response = await getProducts();
        setProducts(response.data);
        // Initialize order items with product IDs and quantity 0
        setOrder((prevOrder) => ({
          ...prevOrder,
          items: response.data.map((product) => ({
            product_id: product.id,
            quantity: 0,
          })),
        }));
      } catch (error) {
        console.error("Error fetching products:", error);
      }
    };
    fetchProducts();
  }, []);

  const handleQuantityChange = (productId, delta) => {
    setOrder((prevOrder) => ({
      ...prevOrder,
      items: prevOrder.items.map((item) =>
        item.product_id === productId
          ? { ...item, quantity: Math.max(0, item.quantity + delta) }
          : item
      ),
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const filteredItems = order.items.filter((item) => item.quantity > 0);
      if (filteredItems.length === 0) {
        setMessage("Please select at least one product.");
        return;
      }
      await placeOrder({ ...order, items: filteredItems });
      setMessage("Order placed successfully!");
      setOrder({ customer_name: "", items: [] });
    } catch (error) {
      setMessage(error.response?.data?.detail || "Error placing order");
    }
  };

  return (
    <div>
      <h2>Place Order</h2>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Customer Name"
          value={order.customer_name}
          onChange={(e) => setOrder({ ...order, customer_name: e.target.value })}
          required
        />
        <div>
          <h3>Products</h3>
          {products.map((product) => (
            <div key={product.id}>
              <span>
                {product.name} - Rs.{product.price_per_unit} quantity available: {product.unit}
              </span>
              <br></br>
              <center>
              <button
                type="button"
                onClick={() => handleQuantityChange(product.id, -1)}
              >
                -
              </button>
              <span>
                {
                  order.items.find((item) => item.product_id === product.id)
                    ?.quantity || 0
                }
              </span> quantity to order
              <button
                type="button"
                onClick={() => handleQuantityChange(product.id, 1)}
              >
                +
              </button>
              </center>
            </div>
          ))}
        </div>
        <button type="submit">Place Order</button>
      </form>
      {message && <p>{message}</p>}
    </div>
  );
}

export default PlaceOrder;