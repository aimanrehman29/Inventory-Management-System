from product import Product, Electronics, Clothing, Grocery

class Inventory:
    def __init__(self):
        self._product = {}  

    def add_product(self, product: Product):
        if product._product_id in self._product:
            raise ValueError("Product with this ID already exists.")
        self._product[product._product_id] = product

    def remove_product(self, product_id):
        if product_id not in self._product:
            raise ValueError("Product not found.")  
        del self._product[product_id] 

    def search_by_name(self, name):
        return [product for product in self._product.values() if name.lower() in product._name.lower()] 

    def search_by_type(self, product_type):
        return [product for product in self._product.values() if isinstance(product, product_type)]

    def list_all_products(self):
        return [str(product) for product in self._product.values()]

    def sell_product(self, product_id, quantity):
        if product_id not in self._product:
            raise ValueError("Product not found.")  
        product = self._product[product_id]
        product.sell(quantity)

    def restock_product(self, product_id, quantity):
        if product_id not in self._product:
            raise ValueError("Product not found.") 
        product = self._product[product_id]
        product.restock(quantity)

    def total_inventory_value(self):
        return sum(product.get_total_value() for product in self._product.values()) 

    def remove_expired_products(self):
        expired_products = [product_id for product_id, product in self._product.items() if isinstance(product, Grocery) and product.is_expired()]
        for product_id in expired_products:
            del self._product[product_id] 
