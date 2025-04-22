def count_even(lst):
    # Count even numbers in the list
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"There are {even_count} even numbers.")  # Display the count

def main():
    lst = []  # Empty list for storing numbers

    # Get input from user until they press Enter
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":  # Stop if Enter is pressed without a number
            break
        try:
            lst.append(int(user_input))  # Add number to list
        except ValueError:
            print("Invalid input. Please enter an integer.")  # Handle invalid input

    count_even(lst)  # Count and display even numbers

main()  # Run the program
