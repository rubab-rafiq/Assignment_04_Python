def print_ones_digit(num):
    # Extract the ones digit using the modulo operator
    ones_digit = num % 10
    # Print the result
    print(f"The ones digit is {ones_digit}")

def main():
    # Prompt the user for an integer
    num = int(input("Enter a number: "))
    # Call the function to print the ones digit
    print_ones_digit(num)

# This provided line is required at the end of the Python file to call the main() function.
if __name__ == '__main__':
    main()
