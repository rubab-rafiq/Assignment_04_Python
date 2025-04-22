# Function to perform the doubling process
def main():
    # Ask the user to enter a number
    curr_value = int(input("Enter a number: "))
    
    # While loop to double the number until it's 100 or more
    while curr_value < 100:
        curr_value = curr_value * 2  # Double the number
        print(curr_value, end=" ")    # Print the current doubled value

# Ensures that the main function runs only when this script is executed directly
if __name__ == '__main__':
    main()  # Call the main function
