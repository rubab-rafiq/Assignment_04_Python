def print_multiple(message, repeats):
    # Print the message the specified number of times
    for _ in range(repeats):
        print(message)

def main():
    # Ask the user for a message and a number of repeats
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    
    # Call the function to print the message the specified number of times
    print_multiple(message, repeats)

# This line ensures the program runs when executed directly
if __name__ == '__main__':
    main()
