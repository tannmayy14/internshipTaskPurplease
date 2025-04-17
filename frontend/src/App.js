import React from "react";
import AddProduct from "./components/AddProduct";
import ProductList from "./components/ProductList";
import PlaceOrder from "./components/PlaceOrder";
import OrderList from "./components/OrderList";
import './App.css';

function App() {
  return (
    <div>
      <h1>Smart Grocery Order System</h1>
      <AddProduct />
      <ProductList />
      <PlaceOrder />
      <OrderList />
    </div>
  );
}

export default App;