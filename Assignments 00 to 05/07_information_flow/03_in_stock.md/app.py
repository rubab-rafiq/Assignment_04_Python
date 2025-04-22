# Function that returns the number of a fruit in stock
def num_in_stock(fruit):
    # Inventory of fruits and their stock
    inventory = {
        "pear": 1000,
        "apple": 500,
        "banana": 1500,
        "grape": 300,
        "orange": 0  # Example where the fruit is out of stock
    }
    
    # Return the stock of the requested fruit or 0 if not in inventory
    return inventory.get(fruit, 0)

def main():
    # Ask the user to enter a fruit
    fruit = input("Enter a fruit: ").lower()  # Converting to lowercase to handle case sensitivity
    
    # Get the number of that fruit in stock
    stock_count = num_in_stock(fruit)
    
    # Print appropriate message based on stock count
    if stock_count > 0:
        print("This fruit is in stock! Here is how many:")
        print(stock_count)
    else:
        print("This fruit is not in stock.")

# This provided line is required at the end of Python file to call the main() function
if __name__ == '__main__':
    main()
