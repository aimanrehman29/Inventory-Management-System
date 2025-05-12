from inventory import Inventory
from product import Electronics, Grocery, Clothing
from utils import save_inventory, load_inventory
from exceptions import InsufficientStockError, ProductAlreadyExistsError

def show_menu():
    print("\nInventory Management System Menu:")
    print("1. Add Product")
    print("2. Sell Product")
    print("3. View Products")
    print("4. Save Inventory")
    print("5. Load Inventory")
    print("6. Exit")

def main():
    inventory = Inventory()

    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            product_type = input("Enter product type (Electronics/Grocery/Clothing): ").lower()
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity in stock: "))
            
            if product_type == 'electronics':
                warranty = int(input("Enter warranty years: "))
                brand = input("Enter brand: ")
                product = Electronics(product_id, name, price, quantity, warranty, brand)
                try:
                    inventory.add_product(product)
                    print("Product added successfully!")
                except ProductAlreadyExistsError as e:
                    print(e)
            elif product_type == 'grocery':
                expiry_date = input("Enter expiry date (YYYY-MM-DD): ")
                product = Grocery(product_id, name, price, quantity, expiry_date)
                try:
                    inventory.add_product(product)
                    print("Product added successfully!")
                except ProductAlreadyExistsError as e:
                    print(e)
            elif product_type == 'clothing':
                size = input("Enter size: ")
                material = input("Enter material: ")
                product = Clothing(product_id, name, price, quantity, size, material)
                try:
                    inventory.add_product(product)
                    print("Product added successfully!")
                except ProductAlreadyExistsError as e:
                    print(e)
            else:
                print("Invalid product type!")

        elif choice == '2':
            product_id = input("Enter product ID to sell: ")
            quantity = int(input("Enter quantity to sell: "))
            try:
                inventory.sell_product(product_id, quantity)
                print("Product sold successfully!")
            except (ValueError, InsufficientStockError) as e:
                print(e)

        elif choice == '3':
            print("All Products:")
            products = inventory.list_all_products()
            for product in products:
                print(product)

        elif choice == '4':
            filename = input("Enter filename to save inventory: ")
            save_inventory(inventory, filename)

        elif choice == '5':
            filename = input("Enter filename to load inventory: ")
            load_inventory(inventory, filename)

        elif choice == '6':
            print("Exiting system...")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
