# 05_remainder_division.md
# Commit: Add program to divide two integers and show quotient and remainder
# This program asks the user for two integers and calculates
# the quotient and remainder using integer division and modulus.

def main():
    num1 = int(input("\033[1;3mPlease enter an integer to be divided: \033[0m"))
    num2 = int(input("\033[1;3mPlease enter an integer to divide by: \033[0m"))
    
    quotient = num1 // num2
    remainder = num1 % num2
    
    print(f"\nThe result of this division is {quotient} with a remainder of {remainder}")

if __name__ == "__main__":
    main()
