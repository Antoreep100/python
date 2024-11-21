menu = {  # Define the Menu of Restaurant
    'Pizza': 100,
    'Pasta': 300,
    'Burger': 50,
    'Salad': 80,
    'Coffee': 120,
}

# Greeting
print("Welcome to my Restaurant!")
print("Menu:")
for item, price in menu.items():
    print(f"{item}: BDT{price}")

order_total = 0  # Initialize order total

# Get the first item
item_1 = input("Enter the name of the item you want to order: ")
if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item '{item_1}' has been added to your order.")
else:
    print(f"Ordered item '{item_1}' is not available.")

# Ask if the user wants to add another item
another_order = input("Do you want to add another item? (Yes/No): ").strip().capitalize()
if another_order == "Yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your item '{item_2}' has been added to your order.")
    else:
        print(f"Ordered item '{item_2}' is not available.")

# Display the total amount
print(f"The total amount for your order is BDT{order_total}")
