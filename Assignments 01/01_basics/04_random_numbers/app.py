import random

def main():
    for _ in range(10):
        # Generate a random number between 1 and 100 (inclusive)
        value = random.randint(1, 100)
        print(value, end=' ')  # Print on the same line with space

# Run the program
if __name__ == '__main__':
    main()
