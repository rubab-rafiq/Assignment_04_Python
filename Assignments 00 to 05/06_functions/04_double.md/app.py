def double(num):
    # Multiply the number by 2 and return the result
    return num * 2

def main():
    # Ask the user for a number
    num = float(input("Enter a number: "))  # Use float to handle both integer and decimal inputs
    result = double(num)  # Call the double function with the user input
    print(f"Double that is {result}")  # Print the result

# Run the program
main()
