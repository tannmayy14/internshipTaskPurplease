import axios from "axios";

const API_BASE_URL = "http://localhost:8000"; // Replace with your backend URL

export const addProduct = (product) => axios.post(`${API_BASE_URL}/products`, product);
export const getProducts = () => axios.get(`${API_BASE_URL}/products`);
export const placeOrder = (order) => axios.post(`${API_BASE_URL}/orders`, order);
export const getOrders = () => axios.get(`${API_BASE_URL}/orders`);