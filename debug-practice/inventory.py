def add_item(inventory, item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"Added {quantity} of {item_name}. Total: {inventory[item_name]}")

def remove_item(inventory, item_name, quantity):
    
    if item_name not in inventory:
        print(f"Error: {item_name} does not exist in inventory.")
        return
    
    if inventory[item_name] < quantity:
        print(f"Error: Not enough stock of {item_name} to remove.")
        return
    
    if inventory[item_name] == 0:
        print(f"{item_name} is out of stock.")
        return
        
    inventory[item_name] -= quantity
    print(f"Removed {quantity} of {item_name}. Remaining: {inventory[item_name]}")

def check_stock(inventory, item_name):
    if item_name in inventory:
        print(f"{item_name} in stock")
    else:
        print(f"{item_name} is out of stock.")

def main():
    inventory = {}  # Dictionary to store inventory items and their quantities
    while True:
        print("\nInventory Management System")
        print("1. Add item")
        print("2. Remove item")
        print("3. Check stock")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            add_item(inventory, item_name, quantity)
            
        elif choice == "2":
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity to remove: "))
            remove_item(inventory, item_name, quantity)
            
        elif choice == "3":
            item_name = input("Enter item name: ")
            check_stock(inventory, item_name)
            
        elif choice == "4":
            print("Exiting program.")
            break
            
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    # There are two bugs in this program.
    # BUG: add 10 apples. Remove 15 apples. Does that output look right to you? 
    #    also, "Check stock" on apples after removing the 15. Bug?
    # BUG: Start over. Add 10 oranges. Remove 10 oranges. Check Stock on oranges. Bug?
    main()
