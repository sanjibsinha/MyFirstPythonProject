inventory = {} # dictionary to store the inventory

def add_item(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity

    print(f"{quantity} {item} added to inventory.")

def remove_item(item, quantity):
    if item in inventory:
        if inventory[item] >= quantity:
            inventory[item] -= quantity
            print(f"{quantity} {item} removed from inventory.")
        else:
            print(f"Cannot remove {quantity} {item} from inventory. Only {inventory[item]} in stock.")
    else:
        print(f"{item} not in inventory.")

def display_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print("Current Inventory:")
    for item, quantity in inventory.items():
        print(f"{item}: {quantity}")

# main proram loop
while True:
    print("\nInventory Management System")
    print("1. Add item to inventory")
    print("2. Remove item from inventory")
    print("3. Display inventory")
    print("4. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        item = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        add_item(item, quantity)
    elif choice == "2":
        item = input("Enter item: ")
        quantity = int(input("Enter quantity: "))
        remove_item(item, quantity)
    elif choice == "3":
        display_inventory()
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")

print("Exiting Inventory Management System.")

# end of inventory.py
