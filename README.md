## SmartSoft POS Software - Backend API Documentation

SmartSoft is a comprehensive point-of-sale software application that manages users, products, sales, purchases, stock, and other entities essential to store management.

### Base URL The base URL for accessing the API is:

arduino Copy code https://smart-soft.onrender.com/ Features


## Features

### 1. User Management
- User Registration
#####    Endpoint: /owners/register/
#####    Allows new users to register an account.

User Login
#####    Endpoint: /owners/login/
######   Allows existing users to log in with their credentials.

### 2. Sell Product
- Sell Product to a Customer
#####    Endpoint: /purchases/sale/{owner_id}/
######    Allows the user to sell a product to a customer.

- View Sell List
#####    Endpoint: /purchases/sale/report/?owner_id={owner_id}
######    Provides a report of all sales for a specific owner.

## 3. Purchase Product
- Purchase Product from Supplier
#####    Endpoint: /purchases/product/{owner_id}/
######    Allows the user to purchase products from suppliers.

- View Purchase List
#####    Endpoint: /purchases/report/?owner_id={owner_id}
######    Provides a report of all purchases for a specific owner.

## 4. Product Management
- Add New Product
#####    Endpoint: /products/add/product/{owner_id}/
######    Allows the user to add a new product to the inventory.

- View Product List
#####    Endpoint: /products/all/product/?owner_id={owner_id}
######    Displays a list of all products for a specific owner.

- View Single Product
#####    Endpoint: /products/single/product/{product_id}/
######    Shows details of a specific product by product ID.

## 5. Category Management
- Add New Category
#####    Endpoint: /products/add/category/{owner_id}/
######    Allows the user to add a new product category.

- View Category List
#####    Endpoint: /products/all/category/?owner_id={owner_id}
######    Displays a list of all categories for a specific owner.

- View Single Category
#####    Endpoint: /products/category/{category_id}/
######    Shows details of a specific category by category ID.

## 6. Brand Management
- Add New Brand
#####    Endpoint: /products/add/brand/{owner_id}/
######    Allows the user to add a new brand.

- View Brand List
#####    Endpoint: /products/all/brand/?owner_id={owner_id}
######    Displays a list of all brands for a specific owner.

- View Single Brand
#####    Endpoint: /products/brand/{brand_id}/
######    Shows details of a specific brand by brand ID.

## 7. Unit Management
- Add New Unit
#####    Endpoint: /products/add/unit/{owner_id}
######    Allows the user to add a new unit.

- View Unit List
#####    Endpoint: /products/all/unit/?owner_id={owner_id}
######    Displays a list of all units for a specific owner.

- View Single Unit
#####    Endpoint: /products/unit/{unit_id}/
######    Shows details of a specific unit by unit ID.

## 8. Stock Management
- View Stock Details
#####    Endpoint: /stocks/show/?owner_id={owner_id}
######    Shows details of available stock with product details.

## 9. Customer Management
- Add New Customer
#####    Endpoint: /peoples/add/customer/{owner_id}/
######    Allows the user to add a new customer.

- View Customer List
#####    Endpoint: /peoples/all/customer/?owner_id={owner_id}
######    Displays a list of all customers for a specific owner.

- View Customer Due Report
#####    Endpoint: /peoples/customer/due/report/?owner_id={owner_id}
######    Shows a report of due amounts from each customer.

- View Single Customer
#####    Endpoint: /peoples/edit/customer/{customer_id}/
######    Shows details of a specific customer by customer ID.

## 10. Supplier Management
- Add New Supplier
#####    Endpoint: /peoples/add/supplier/{owner_id}/
######    Allows the user to add a new supplier.

- View Supplier List
#####    Endpoint: /peoples/all/supplier/?owner_id={owner_id}
######    Displays a list of all suppliers for a specific owner.

- View Supplier Due Report
#####    Endpoint: /peoples/supplier/due/report/?owner_id={owner_id}
######    Shows a report of due amounts for each supplier.

-View Single Supplier
#####    Endpoint: /peoples/edit/supplier/{supplier_id}/
######    Shows details of a specific supplier by supplier ID.

## 11. Employee Management
- Add New Employee
#####    Endpoint: /peoples/add/employee/{owner_id}/
######    Allows the user to add a new employee.

- View Employee List
#####    Endpoint: /peoples/all/employee/?owner_id={owner_id}
######    Displays a list of all employees for a specific owner.

- View Single Employee
#####    Endpoint: /peoples/edit/employee/{employee_id}/
######    Shows details of a specific employee by employee ID.

## 12. Salary Management
- Pay Salary to Employees
#####    Endpoint: /peoples/salary/{owner_id}/
######    Allows the user to pay salaries to employees.

- View Salary Report
#####    Endpoint: /peoples/salary/report/?owner_id={owner_id}
######    Shows a report of salary payments.


## Notes
- Replace {owner_id}, {product_id}, {category_id}, {brand_id}, {unit_id}, {customer_id}, {supplier_id}, {employee_id} with the respective ID values for the owner or entity.
- Make sure the owner is authenticated before accessing protected endpoints.
