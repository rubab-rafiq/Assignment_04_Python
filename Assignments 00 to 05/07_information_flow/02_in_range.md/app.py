def in_range(n, low, high):
    # Returns True if n is between low and high, inclusive
    return low <= n <= high

def main():
    # Example usage
    n = int(input("Enter a number: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    # Check if the number is within the range
    print(in_range(n, low, high))

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
