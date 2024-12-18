## Project Overview
This project involves creating a clone of Amazon's web application. It includes features such as user authentication, product listings, a shopping cart, and an inventory management system. The project is built using the following technologies:

Backend: Django (Python)
Frontend: React (JavaScript)
Database: MySQL

## Features
User Authentication (Sign Up, Login, Logout)
Product Listing and Search
Product Detail View
Shopping Cart Functionality
Inventory Management System for Admin
Order Management
Purchase Order
Sales order
Supplier
Warehouse Management
User Management
Multi Level Ecommerce Website
Responsive Design
## Getting Started
### Prerequisites
Ensure the following tools and software are installed on your local development machine:

- **Python** (>= 3.6)  
- **Node.js** (>= 14.0)  
- **npm** (>= 6.0)  
- **Django** (>= 5.0)  
- **React** (>= 17.0)  
- **MySQL Server**

## Installation
1.Clone the Repository

  #### For Backend:

    cd backend
    python -m venv venv
    source ../venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    pip install -r requirements.txt

#### DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

    python manage.py migrate
    python manage.py runserver


#### For Frontend:
```bash
 cd ../frontend
 npm install
 npm start
