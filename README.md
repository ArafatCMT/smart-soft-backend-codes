<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>SmartSoft POS Software - Backend API Documentation</title>
</head>
<body>
    <h1>SmartSoft POS Software - Backend API Documentation</h1>
    <p>SmartSoft is a comprehensive point-of-sale software application that manages users, products, sales, purchases, stock, and other entities essential to store management.</p>

    <h2>Base URL</h2>
    <p>The base URL for accessing the API is:</p>
    <code>https://smart-soft.onrender.com/</code>

    <h2>Features</h2>

    <h3>1. User Management</h3>
    <ul>
        <li><strong>User Registration</strong><br>Endpoint: <code>/owners/register/</code><br>Allows new users to register an account.</li>
        <li><strong>User Login</strong><br>Endpoint: <code>/owners/login/</code><br>Allows existing users to log in with their credentials.</li>
    </ul>

    <h3>2. Sell Product</h3>
    <ul>
        <li><strong>Sell Product to a Customer</strong><br>Endpoint: <code>/purchases/sale/{owner_id}/</code><br>Allows the user to sell a product to a customer.</li>
        <li><strong>View Sell List</strong><br>Endpoint: <code>/purchases/sale/report/?owner_id={owner_id}</code><br>Provides a report of all sales for a specific owner.</li>
    </ul>

    <h3>3. Purchase Product</h3>
    <ul>
        <li><strong>Purchase Product from Supplier</strong><br>Endpoint: <code>/purchases/product/{owner_id}/</code><br>Allows the user to purchase products from suppliers.</li>
        <li><strong>View Purchase List</strong><br>Endpoint: <code>/purchases/report/?owner_id={owner_id}</code><br>Provides a report of all purchases for a specific owner.</li>
    </ul>

    <h3>4. Product Management</h3>
    <ul>
        <li><strong>Add New Product</strong><br>Endpoint: <code>/products/add/product/{owner_id}/</code><br>Allows the user to add a new product to the inventory.</li>
        <li><strong>View Product List</strong><br>Endpoint: <code>/products/all/product/?owner_id={owner_id}</code><br>Displays a list of all products for a specific owner.</li>
        <li><strong>View Single Product</strong><br>Endpoint: <code>/products/single/product/{product_id}/</code><br>Shows details of a specific product by product ID.</li>
    </ul>

    <h3>5. Category Management</h3>
    <ul>
        <li><strong>Add New Category</strong><br>Endpoint: <code>/products/add/category/{owner_id}/</code><br>Allows the user to add a new product category.</li>
        <li><strong>View Category List</strong><br>Endpoint: <code>/products/all/category/?owner_id={owner_id}</code><br>Displays a list of all categories for a specific owner.</li>
        <li><strong>View Single Category</strong><br>Endpoint: <code>/products/category/{category_id}/</code><br>Shows details of a specific category by category ID.</li>
    </ul>

    <h3>6. Brand Management</h3>
    <ul>
        <li><strong>Add New Brand</strong><br>Endpoint: <code>/products/add/brand/{owner_id}/</code><br>Allows the user to add a new brand.</li>
        <li><strong>View Brand List</strong><br>Endpoint: <code>/products/all/brand/?owner_id={owner_id}</code><br>Displays a list of all brands for a specific owner.</li>
        <li><strong>View Single Brand</strong><br>Endpoint: <code>/products/brand/{brand_id}/</code><br>Shows details of a specific brand by brand ID.</li>
    </ul>

    <h3>7. Unit Management</h3>
    <ul>
        <li><strong>Add New Unit</strong><br>Endpoint: <code>/products/add/unit/{owner_id}</code><br>Allows the user to add a new unit.</li>
        <li><strong>View Unit List</strong><br>Endpoint: <code>/products/all/unit/?owner_id={owner_id}</code><br>Displays a list of all units for a specific owner.</li>
        <li><strong>View Single Unit</strong><br>Endpoint: <code>/products/unit/{unit_id}/</code><br>Shows details of a specific unit by unit ID.</li>
    </ul>

    <h3>8. Stock Management</h3>
    <ul>
        <li><strong>View Stock Details</strong><br>Endpoint: <code>/stocks/show/?owner_id={owner_id}</code><br>Shows details of available stock with product details.</li>
    </ul>

    <h3>9. Customer Management</h3>
    <ul>
        <li><strong>Add New Customer</strong><br>Endpoint: <code>/peoples/add/customer/{owner_id}/</code><br>Allows the user to add a new customer.</li>
        <li><strong>View Customer List</strong><br>Endpoint: <code>/peoples/all/customer/?owner_id={owner_id}</code><br>Displays a list of all customers for a specific owner.</li>
        <li><strong>View Customer Due Report</strong><br>Endpoint: <code>/peoples/customer/due/report/?owner_id={owner_id}</code><br>Shows a report of due amounts from each customer.</li>
        <li><strong>View Single Customer</strong><br>Endpoint: <code>/peoples/edit/customer/{customer_id}/</code><br>Shows details of a specific customer by customer ID.</li>
    </ul>

    <h3>10. Supplier Management</h3>
    <ul>
        <li><strong>Add New Supplier</strong><br>Endpoint: <code>/peoples/add/supplier/{owner_id}/</code><br>Allows the user to add a new supplier.</li>
        <li><strong>View Supplier List</strong><br>Endpoint: <code>/peoples/all/supplier/?owner_id={owner_id}</code><br>Displays a list of all suppliers for a specific owner.</li>
        <li><strong>View Supplier Due Report</strong><br>Endpoint: <code>/peoples/supplier/due/report/?owner_id={owner_id}</code><br>Shows a report of due amounts for each supplier.</li>
        <li><strong>View Single Supplier</strong><br>Endpoint: <code>/peoples/edit/supplier/{supplier_id}/</code><br>Shows details of a specific supplier by supplier ID.</li>
    </ul>

    <h3>11. Employee Management</h3>
    <ul>
        <li><strong>Add New Employee</strong><br>Endpoint: <code>/peoples/add/employee/{owner_id}/</code><br>Allows the user to add a new employee.</li>
        <li><strong>View Employee List</strong><br>Endpoint: <code>/peoples/all/employee/?owner_id={owner_id}</code><br>Displays a list of all employees for a specific owner.</li>
        <li><strong>View Single Employee</strong><br>Endpoint: <code>/peoples/edit/employee/{employee_id}/</code><br>Shows details of a specific employee by employee ID.</li>
    </ul>

    <h3>12. Salary Management</h3>
    <ul>
        <li><strong>Pay Salary to Employees</strong><br>Endpoint: <code>/peoples/salary/{owner_id}/</code><br>Allows the user to pay salaries to employees.</li>
        <li><strong>View Salary Report</strong><br>Endpoint: <code>/peoples/salary/report/?owner_id={owner_id}</code><br>Shows a report of salary payments.</li>
    </ul>

    <h3>Notes</h3>
    <p>Replace <code>{owner_id}</code>, <code>{product_id}</code>, <code>{category_id}</code>, <code>{brand_id}</code>, <code>{unit_id}</code>, <code>{customer_id}</code>, <code>{supplier_id}</code>, <code>{employee_id}</code> with the respective ID values for the owner or entity. Ensure the owner is authenticated before accessing protected endpoints.</p>
</body>
</html>
