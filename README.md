## SmartSoft POS Software - Backend API Documentation

SmartSoft is a comprehensive point-of-sale software application that manages users, products, sales, purchases, stock, and other entities essential to store management

### Base URL The base URL for accessing the API is:

arduino Copy code https://smart-soft.onrender.com/ Features


## Features

### 1. User Management
- User Registration
#####    Endpoint: /owners/register/
#####    Allows new users to register an account.

User Login
#####    Endpoint: /owners/login/
#####    Allows existing users to log in with their credentials.

### 2. Sell Product
- Sell Product to a Customer
#####    Endpoint: /purchases/sale/{owner_id}/
#####    Allows the user to sell a product to a customer.

- View Sell List
#####    Endpoint: /purchases/sale/report/?owner_id={owner_id}
#####    Provides a report of all sales for a specific owner.

## 3. Purchase Product
- Purchase Product from Supplier
#####    Endpoint: /purchases/product/{owner_id}/
#####    Allows the user to purchase products from suppliers.

- View Purchase List
#####    Endpoint: /purchases/report/?owner_id={owner_id}
#####    Provides a report of all purchases for a specific owner.

## 4. Product Management
- Add New Product
#####    Endpoint: /products/add/product/{owner_id}/
#####    Allows the user to add a new product to the inventory.

- View Product List
#####    Endpoint: /products/all/product/?owner_id={owner_id}
#####    Displays a list of all products for a specific owner.

- View Single Product
#####    Endpoint: /products/single/product/{product_id}/
#####    Shows details of a specific product by product ID.
