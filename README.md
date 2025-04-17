# Smart Grocery Order API System

This project was carried out by me as an evaluation task for internship offered by Purplease.  
It is a RESTful backend for a basic grocery ordering system, built using **FastAPI**. The system allows users to manage products, place orders, and view order details.  
Additionally, the project includes a simple React-based frontend for better understanding and interaction with the API.

---

## Features

### Core Functionality
1. **Add Products**  
   - **Endpoint**: `POST /products`  
   - Validates unique product names and ensures price is a positive number.  
   - Stores product data in a JSON file.

2. **View Product List**  
   - **Endpoint**: `GET /products`  
   - Retrieves all available products.

3. **Place Orders**  
   - **Endpoint**: `POST /orders`  
   - Validates product IDs and ensures quantities are positive integers.  
   - Calculates the total amount for each order.  
   - Stores order data in a JSON file.

4. **View Order List**  
   - **Endpoint**: `GET /orders`  
   - Retrieves all orders with detailed information, including total amounts.

---

### Bonus Features
- **Swagger/OpenAPI Documentation**  
  - Auto-generated API documentation available at `http://localhost:8000/docs`.

- **Unit Tests**  
  - Comprehensive unit tests for product addition and order logic.  
  - To run tests, use the following command:  
    ```bash
    pytest tests/
    ```

- **Simple React Frontend**  
  - A basic UI to interact with the API, including components for adding products, viewing products, placing orders, and viewing orders.

- **Data Persistence**  
  - Product and order data are stored in JSON files (`products.json` and `orders.json`).

---

## How to Run

### Backend
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
2. Start the Server
    ```bash
    python main.py
3. Access the API documentation at
    http://localhost:8000/docs

### Testing
1. Run the unit tests using the following command:
    ```bash
    pytest tests/

### Screenshots
1. API Documentation 
![localhost_docs](https://github.com/user-attachments/assets/6bdd47ee-52fa-4dba-a454-9152ae3744f9)

2. Tests
![testPassed](https://github.com/user-attachments/assets/b3ce64fd-15be-4fd1-97b1-ba75fc781f3f)


### Frontend
1. Navigate to the frontend directory:
    ```bash
    cd frontend
2. Install dependencies:
    ```bash
    npm install
3. Start the React development server:
    ```bash
    npm start
4. Access the frontend at http://localhost:3000


