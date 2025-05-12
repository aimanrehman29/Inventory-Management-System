# **Inventory Management System**

### ✅ **Features**

- **Add Products** – Add products of type `Electronics`, `Grocery`, or `Clothing` to the inventory.
- **Sell Products** – Sell products and automatically update stock levels.
- **Restock Products** – Restock products by increasing the quantity.
- **View Products** – List all products in the inventory with details like price, quantity, and type.
- **Save Inventory** – Save the inventory to a **JSON** file to persist data across sessions.
- **Load Inventory** – Load inventory from a saved **JSON** file.
- **Product Types** – Supports three product types: **Electronics**, **Grocery**, and **Clothing**.

### ✅ **Technology Used**

- **Python** – The main language used to build the system.
- **pytest** – Testing framework used to validate functionalities.
- **JSON** – Data persistence format for saving/loading inventory.
- **Custom Exceptions** – To handle product-related errors (e.g., `InsufficientStockError`, `ProductAlreadyExistsError`, `InvalidProductDataError`).
