# 00_count_nums
# Program to count the frequency of each number in a list
# Using a dictionary to track the number of occurrences

# Dictionary to store the count of each number
number_count = {}

# Asking user to enter numbers until they enter 'done'
while True:
    # Taking user input
    number_input = input("Enter a number (or type 'done' to stop): ")

    # Check if user wants to stop inputting numbers
    if number_input.lower() == 'done':
        break
    
    try:
        # Convert the input to an integer
        number = int(number_input)
        
        # If the number is already in the dictionary, increase its count
        if number in number_count:
            number_count[number] += 1
        else:
            # Otherwise, add the number to the dictionary with count 1
            number_count[number] = 1

    except ValueError:
        # If the input is not a valid number, ask again
        print("Please enter a valid number or 'done' to stop.")

# Printing the count of each number entered
for number, count in number_count.items():
    print(f"{number} appears {count} times.")
