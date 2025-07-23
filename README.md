# Sales Project

## Overview
This project is a Django-based application for managing sales data. It includes models for `Customer`, `Product`, `Order`, and `OrderItem`, along with APIs for accessing sales and product information.

## Features
- **Customer Management**: Keep track of customer details such as name, email, and address.
- **Product Management**: Store product information including name, category, and pricing.
- **Order Management**: Track orders placed by customers, including order date, payment status, and total amount.
- **OrderItem Management**: Store the items included in each order, with quantity sold, product details, and price.
- **API Endpoints**:
  - **Refresh Data**: For Refrsh the data. 
  - **Top Products**: Fetch the top products based on the quantity sold in a given date range.
  - **Revenue Calculation**: Calculate the total revenue between a specified date range.

## Prerequisites
- Python 3.6 or higher
- Django 5.2.4
- SQLite Database (default)

## Installation

### 1. Clone the repository:
```bash
git clone https://github.com/your-username/sales-project.git
cd sales-project

2. Create a Virtual Environment:

python -m venv .venv

3. Activate the Virtual Environment:

.venv\Scripts\activate

4. Install Required Packages:

pip install -r requirements.txt

5.Database Setup

python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

6.Start the Development Server:

python manage.py runserver

API Endpoints

### 1. **Refresh Data**
   - **URL**: `/sales/api/refresh_data/`
   - **Method**: `POST`
   - **Description**: Triggers a data refresh, typically for reloading or updating sales or product data.
   - **Example**:
     ```http
     POST http://127.0.0.1:8000/sales/api/refresh_data/
     ```
   - **Response**: A JSON response with a success message.
     ```json
     {
       "message": "Data refresh triggered successfully"
     }
     ```

---

### How it works:
- **`POST /sales/api/refresh_data/`**: This endpoint triggers a function (e.g., `refresh_data()`) that is usually responsible for updating or reloading sales data. It is useful if you need to perform data updates or recalculations based on changing external data or internal business logic.

---

### Example of Usage:
When a `POST` request is made to `/sales/api/refresh_data/`, it triggers the `refresh_data` function in your application, which could involve tasks such as:
- Recalculating revenue, top products, or other metrics.
- Reloading product or order data from an external source or database.

You can use tools like **Postman** or **cURL** to send a `POST` request to this endpoint.

### Example with cURL:
```bash
curl -X POST http://127.0.0.1:8000/sales/api/refresh_data/
Expected Response:
{
  "message": "Data refresh triggered successfully"
}



### 2. **Get Revenue**
   - **URL**: `/sales/api/revenue/?start_date=2023-01-01&end_date=2023-12-31`
   - **Method**: `GET`
   - **Query Params**: `start_date`, `end_date`
   - **Description**: Calculates the total revenue between a specified date range.
   - **Example**:
     ```http
     GET http://127.0.0.1:8000/sales/api/revenue/?start_date=2024-01-01&end_date=2024-12-31
     ```

### 3. **Get Top Products**
   - **URL**: `/sales/api/top_products/?start_date=2023-01-01&end_date=2023-12-31`
   - **Method**: `GET`
   - **Query Params**: `start_date`, `end_date`
   - **Description**: Fetches the top products based on the quantity sold between the specified dates.
   - **Example**:
     ```http
     GET http://127.0.0.1:8000/sales/api/top_products/?start_date=2024-01-01&end_date=2024-12-31
     ```
