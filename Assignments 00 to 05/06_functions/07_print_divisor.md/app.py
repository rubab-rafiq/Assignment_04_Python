def print_divisors(num):
    # Print divisors of the given number
    print(f"Here are the divisors of {num}")
    
    # Loop through numbers from 1 to num to find divisors
    for i in range(1, num + 1):
        if num % i == 0:  # If there's no remainder, i is a divisor
            print(i, end=" ")

def main():
    # Ask user for a number
    num = int(input("Enter a number: "))
    
    # Call the function to print divisors
    print_divisors(num)

# This provided line is required at the end to call main()
if __name__ == '__main__':
    main()
