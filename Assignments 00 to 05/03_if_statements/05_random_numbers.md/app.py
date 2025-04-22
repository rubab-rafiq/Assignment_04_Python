import random  # Importing the 'random' library, which helps in generating random numbers

# Defining constants
N_NUMBERS: int = 10  # We will generate 10 random numbers
MIN_VALUE: int = 1    # The minimum value allowed for the random number (1)
MAX_VALUE: int = 100  # The maximum value allowed for the random number (100)

def main():
   
    # Running a loop for N_NUMBERS (10 times)
    for i in range(N_NUMBERS):
        # Generating a random number in the range between MIN_VALUE and MAX_VALUE
        generate_number = random.randint(MIN_VALUE, MAX_VALUE)
        
        # Printing the generated random number, with a new line after each number
        print(generate_number)

# If the script is being run directly, the main function is called
if __name__ == '__main__':
    main()
