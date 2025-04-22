# Dictionary storing the price of each fruit
fruit_prices = {
    "apple": 2.0,
    "durian": 5.0,
    "jackfruit": 3.0,
    "kiwi": 4.0,
    "rambutan": 6.5,
    "mango": 3.5
}

# Define the main function that contains the program logic
def main():
    total_cost = 0  # Initialize total cost

    # Loop through each fruit and ask the user for quantity
    for fruit, price in fruit_prices.items():
        # Get the number of fruits the user wants
        quantity = int(input(f"How many ({fruit}) do you want?: "))
        # Add the cost of this fruit to the total
        total_cost += quantity * price

    # Print the total cost
    print("Your total is $" + str(total_cost))

# Check if the script is being run directly
if __name__ == '__main__':
    main()
