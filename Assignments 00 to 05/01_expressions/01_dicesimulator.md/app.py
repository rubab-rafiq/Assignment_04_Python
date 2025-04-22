# 01_dicesimulator.md

# Importing the random module to generate random numbers (used for dice rolls)
import random

# Setting the number of sides for each die
Num_Sides = 6

# This function simulates rolling two dice and prints their values and the total
def roll_dice():
    # Generate a random number between 1 and 6 for the first die
    die1 = random.randint(1, Num_Sides)
    
    # Generate a random number between 1 and 6 for the second die
    die2 = random.randint(1, Num_Sides)
    
    # Calculate the total of both dice
    total = die1 + die2

    # Print the values of both dice and their total
    print(f'Die 1: {die1}, Die 2: {die2}, Total: {total}')

# The main function where the program starts executing
def main():
    # Declare a local variable die1 and assign it a value of 10 (this is separate from the die1 inside roll_dice)
    die1 = 10

    # Print the starting value of die1 in main
    print(f'die1 in main() start as: {die1}')

    # Run the roll_dice function 3 times using a loop
    for i in range(3):
        # Call the function to simulate rolling dice
        roll_dice()
        
        # Print the value of die1 again to show that it hasn’t changed
        print(f'die1 in main() end as: {die1}')

# This ensures that main() runs only when the script is executed directly
if __name__ == "__main__":
    main()
