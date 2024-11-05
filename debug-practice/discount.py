# A list of items in a shopping cart with their prices
items = [
    {'name': 'Laptop', 'price': 1200},
    {'name': 'Phone', 'price': 800},
    {'name': 'Headphones', 'price': 150}, # was 'unit price'
    {'name': 'Monitor', 'price': 300},
    {'name': 'Mouse', 'price': 50}
]

# A function to apply a discount to an item if it meets certain conditions
def apply_discount(item, discount_percentage):
    discount = item['price'] * (discount_percentage / 100)
    new_price = item['price'] - discount
    return new_price

# Function to calculate the total price of all items in the cart
def calculate_total(cart):
    total_price = 0
    for i in range(len(cart)):
        total_price += apply_discount(cart[i], 10)
    return total_price

# A function to find the most expensive item in the cart
def find_most_expensive(cart):
    most_expensive = None
    highest_price = 0
    for i in range(len(cart)):
        if cart[i]['price'] > highest_price:
            highest_price = cart[i]['price']
            most_expensive = cart[i]
    return most_expensive

# Main program that calculates the total and finds the most expensive item
def main():
    cart = items

    # Calculate the total price with discounts
    total = calculate_total(cart)
    print(f"Total price after discounts: {total}")

    # Find the most expensive item
    expensive_item = find_most_expensive(cart)
    print(f"The most expensive item is: {expensive_item['name']} which costs {expensive_item['price']}")

if __name__ == "__main__":
    # BUG: This program will crash when you run it.
    main()
