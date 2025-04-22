# Function to calculate the average of two numbers
def calculate_average(num1, num2):
    average = (num1 + num2) / 2  # Calculate the average
    return average  # Return the calculated average

# Main function where user input and calling of calculate_average happens
def main():
    # Test the function by taking two numbers from the user
    num1 = float(input("Enter the first number: "))  # First number input
    num2 = float(input("Enter the second number: "))  # Second number input

    # Call the function and print the result
    result = calculate_average(num1, num2)
    print("The average is:", result)  # Display the average

# Ensures that the main function runs only when this script is executed directly
if __name__ == '__main__':
    main()  # Calling the main function
