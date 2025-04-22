# Constant for the legal age of adulthood
ADULT_AGE = 18

def is_adult(age):
    # Return True if age is greater than or equal to ADULT_AGE, otherwise False
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    # Ask the user for the person's age
    age = int(input("How old is this person?: "))
    
    # Call the is_adult function and print the result
    print(is_adult(age))

# This provided line is required at the end of Python file to call the main() function
if __name__ == '__main__':
    main()
