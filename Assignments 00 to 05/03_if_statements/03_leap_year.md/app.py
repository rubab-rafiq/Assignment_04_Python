# 03_leap_year.md
# Function to check whether the given year is a leap year or not
def check_leap_year(year):
    # Step 1: Check if the year is divisible by 4
    if year % 4 == 0:
        # Step 2: Check if it's also divisible by 100
        if year % 100 == 0:
            # Step 3: If divisible by 400, it's a leap year
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            # It's divisible by 4 but not 100, so it's a leap year
            print("That's a leap year!")
    else:
        # It's not divisible by 4, so it's not a leap year
        print("That's not a leap year.")

# Main function to get input and call check_leap_year
def main():
    # Ask user to input a year
    year = int(input("Enter a year: "))  # Convert input to an integer
    # Call the function to check if it's a leap year
    check_leap_year(year)

# Entry point of the program
if __name__ == "__main__":
    main()
