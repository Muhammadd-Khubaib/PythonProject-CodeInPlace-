products = {}

def add_product(product_id, name, price, stock):
    if product_id in products:
        print(f"Product ID {product_id} already exists.")
    else:
        products[product_id] = {
            "name": name,
            "price": price,
            "stock": stock
        }
        print(f"Product {name} added successfully.")

def display_products():
    if not products:
        print("No products available.")
    else:
        print("\nProducts available:")
        for product_id, details in products.items():
            print(f"ID: {product_id}, Name: {details['name']}, Price: {details['price']}, Stock: {details['stock']}")

def sell_product(product_id, quantity):
    if product_id in products:
        if products[product_id]['stock'] >= quantity:
            products[product_id]['stock'] -= quantity
            print(f"Sold {quantity} of {products[product_id]['name']}.")
        else:
            print(f"Not enough stock to sell {quantity} of {products[product_id]['name']}.")
    else:
        print(f"Product ID {product_id} not found.")

def main():
    while True:
        print("\nMart Management System")
        print("1. Add Product")
        print("2. Display Products")
        print("3. Sell Product")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            product_id = input("Enter product ID: ")
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            add_product(product_id, name, price, stock)
        elif choice == '2':
            display_products()
        elif choice == '3':
            product_id = input("Enter product ID: ")
            quantity = int(input("Enter quantity to sell: "))
            sell_product(product_id, quantity)
        elif choice == '4':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
