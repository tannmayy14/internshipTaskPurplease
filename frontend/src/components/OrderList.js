import React, { useEffect, useState } from "react";
import { getOrders } from "../api";

function OrderList() {
  const [orders, setOrders] = useState([]);

  // Fetch orders from the backend
  const fetchOrders = async () => {
    try {
      const response = await getOrders();
      setOrders(response.data);
    } catch (error) {
      console.error("Error fetching orders:", error);
    }
  };

  useEffect(() => {
    fetchOrders();
  }, []);

  return (
    <div>
      <h2>Order List</h2>
      <ul>
        {orders.map((order) => (
          <li key={order.order_id}>
            <strong>{order.customer_name}</strong> - Total: {order.total_amount}
            <ul>
              {order.items.map((item) => {
                return (
                  <li key={item.product_id}>
                    {item.product_name} - {item.quantity} units
                  </li>
                );
              })}
            </ul>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default OrderList;