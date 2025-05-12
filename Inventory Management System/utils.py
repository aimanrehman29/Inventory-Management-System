import json
from product import Electronics, Grocery, Clothing
from datetime import datetime

def save_inventory(inventory, filename):
    try:
        with open(filename, 'w') as file:
            data = {}
            for product_id, product in inventory._product.items():
                if isinstance(product, Grocery):
                    expiry_date = product._expiry_date.strftime("%Y-%m-%d")  
                else:
                    expiry_date = None  
                
                data[product_id] = {
                    'type': product.__class__.__name__, 
                    'product_id': product._product_id,
                    'name': product._name,
                    'price': product._price,
                    'quantity_in_stock': product._quantity_in_stock,
                    'extra_info': product.__dict__.get('_warranty_years', product.__dict__.get('_size', None)),
                    'expiry_date': expiry_date 
                }
            json.dump(data, file)
        print(f"Inventory saved successfully to {filename}")
    except Exception as e:
        print(f"Error saving inventory: {e}")


def load_inventory(inventory, filename):
    try:
        with open(filename, 'r') as file:
            data = json.load(file) 

            for product_id, product_info in data.items():
                if product_info['type'] == 'Electronics':
                    product = Electronics(
                        product_info['product_id'],
                        product_info['name'],
                        product_info['price'],
                        product_info['quantity_in_stock'],
                        product_info['extra_info'],
                        product_info['name']
                    )
                elif product_info['type'] == 'Grocery':
                    expiry_date = product_info['expiry_date']
                    if isinstance(expiry_date, str):  
                        expiry_date = datetime.strptime(expiry_date, "%Y-%m-%d") 
                    product = Grocery(
                        product_info['product_id'],
                        product_info['name'],
                        product_info['price'],
                        product_info['quantity_in_stock'],
                        expiry_date
                    )
                elif product_info['type'] == 'Clothing':
                    product = Clothing(
                        product_info['product_id'],
                        product_info['name'],
                        product_info['price'],
                        product_info['quantity_in_stock'],
                        product_info['extra_info'],
                        product_info['name']
                    )
                inventory.add_product(product)  
        print(f"Inventory loaded successfully from {filename}")
    except Exception as e:
        print(f"Error loading inventory: {e}")
