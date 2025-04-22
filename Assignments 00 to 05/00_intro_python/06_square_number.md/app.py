# 06_square_number.md

def main():
    # This program calculates the square of a number.
    print("This program calculates the square of a number.")

    # Take number input
    num = float(input("\033[1;3mEnter a number: \033[0m"))

    # Calculate square
    square = num ** 2

    # Display result
    print(f"The square of {num} is {square}")

if __name__ == '__main__':
        main()