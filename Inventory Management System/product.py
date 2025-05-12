from abc import ABC, abstractmethod
import datetime
from exceptions import InsufficientStockError, ProductAlreadyExistsError


class Product(ABC):
    def __init__(self, product_id, name, price, quantity_in_stock):
        self._product_id = product_id
        self._name = name 
        self._price = price
        self._quantity_in_stock = quantity_in_stock

    @abstractmethod 
    def restock(self, amount):
        pass

    @abstractmethod 
    def sell(self, quantity):
        pass

    def get_total_value(self): 
        return self._price * self._quantity_in_stock

    @abstractmethod 
    def __str__(self):
        pass





class Electronics(Product):
    def __init__(self, product_id, name, price, quantity_in_stock,  warranty_years, brand):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.warranty_years = warranty_years
        self.brand = brand

    def restock(self,amount):
        self._quantity_in_stock += amount

    
    def sell(self, quantity):
        if quantity > self._quantity_in_stock:
            raise InsufficientStockError("Not enough stock to sell.") 
        self._quantity_in_stock -= quantity

    def __str__(self):
       return f"Electronics - {self._name}, Brand: {self.brand}, Warranty: {self.warranty_years} years, Price: {self._price}, Stock: {self._quantity_in_stock}"


class Grocery(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, expiry_date):
        super().__init__(product_id, name, price, quantity_in_stock)
        self._expiry_date = datetime.datetime.strptime(expiry_date, "%Y-%m-%d")

    def restock(self, amount):
        self._quantity_in_stock += amount
    
    def sell(self, quantity):
        if quantity > self._quantity_in_stock:
            raise ValueError("Not enough stock to sell.")
        self._quantity_in_stock -= quantity
    
    def is_expired(self):
        return datetime.datetime.now() > self._expiry_date
    
    def __str__(self):
        return f"Grocery - {self._name}, Expiry: {self._expiry_date.strftime('%Y-%m-%d')}, Price: {self._price}, Stock: {self._quantity_in_stock}"



class Clothing(Product):
    def __init__(self, product_id, name, price, quantity_in_stock, size, material):
        super().__init__(product_id, name, price, quantity_in_stock)
        self.size =size
        self.material = material

    def restock(self, amount):
        return super().restock(amount)
    
    def sell(self, quantity):
        return super().sell(quantity)
    
    def __str__(self):
        return f"Clothing - {self._name}, Size: {self.size}, Material: {self.material}, Price: {self._price}, Stock: {self._quantity_in_stock}"