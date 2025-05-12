import pytest
from inventory import Inventory
from product import Electronics, Grocery, Clothing
from exceptions import ProductAlreadyExistsError, InsufficientStockError
from utils import save_inventory, load_inventory
import os
from datetime import datetime

@pytest.fixture
def inventory():
    """Fixture to create a fresh inventory for each test."""
    return Inventory()

# Test 1: Test Adding Products
def test_add_product(inventory):
    """Test that products can be added to the inventory."""
    product = Electronics("E001", "Laptop", 1000, 50, 2, "Dell")
    inventory.add_product(product)
    assert len(inventory._product) == 1
    assert inventory._product["E001"] == product

# Test 2: Test Selling Products
def test_sell_product(inventory):
    """Test that products can be sold and stock is updated correctly."""
    product = Electronics("E001", "Laptop", 1000, 50, 2, "Dell")
    inventory.add_product(product)
    
    inventory.sell_product("E001", 10) 
    assert product._quantity_in_stock == 40  
    
    with pytest.raises(InsufficientStockError):
        inventory.sell_product("E001", 100) 

# Test 3: Test Restocking
def test_restock_product(inventory):
    """Test that products can be restocked."""
    product = Electronics("E001", "Laptop", 1000, 50, 2, "Dell")
    inventory.add_product(product)
    
    inventory.restock_product("E001", 20)  
    assert product._quantity_in_stock == 70 

# Test 4: Test Listing All Products
def test_list_all_products(inventory):
    """Test that all products can be listed."""
    product1 = Electronics("E001", "Laptop", 1000, 50, 2, "Dell")
    product2 = Grocery("G002", "Milk", 2, 100, "2025-12-31")
    
    inventory.add_product(product1)
    inventory.add_product(product2)
    
    all_products = inventory.list_all_products()
    assert len(all_products) == 2
    assert "Laptop" in all_products[0]
    assert "Milk" in all_products[1]

# Test 5: Test Saving and Loading Inventory
def test_save_and_load_inventory(inventory):
    """Test saving and loading inventory to/from a file."""
    product = Electronics("E001", "Laptop", 1000, 50, 2, "Dell")
    inventory.add_product(product)
    
    filename = "test_inventory.json"
    save_inventory(inventory, filename)  
    
    new_inventory = Inventory()
    load_inventory(new_inventory, filename)
    
    # Check if the loaded inventory has the same product
    assert len(new_inventory._product) == 1
    assert new_inventory._product["E001"]._name == "Laptop"
    
   
    os.remove(filename)

