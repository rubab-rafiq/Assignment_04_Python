
# Function to check if the user is tall enough for the ride
def check_height(height):
    # Minimum height requirement for the ride
    MIN_HEIGHT = 50
    
    # Check if the user's height is greater than or equal to the minimum height
    if height >= MIN_HEIGHT:
        print("You're tall enough to ride!")
    else:
        print("You're not tall enough to ride, but maybe next year!")

# Main function to repeatedly ask for user's height
def main():
    while True:
        # Ask the user for their height
        user_input = input("How tall are you? ")  # Get the height as a string
        
        # If the user doesn't enter anything (blank input), break the loop and stop the program
        if user_input == "":
            print("Thank you for checking! Goodbye!")
            break
        
        # Convert user input to a number (integer) and check if it's a valid height
        try:
            height = int(user_input)  # Convert to integer
            check_height(height)  # Check if the user is tall enough
        except ValueError:
            print("Please enter a valid number for your height.")  # If input is not a number

# Entry point of the program
if __name__ == "__main__":
    main()
