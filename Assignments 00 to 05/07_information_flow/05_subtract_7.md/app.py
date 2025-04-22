# Helper function to subtract 7 from a number
def subtract_seven(num):
    return num - 7

def main():
    # Ask the user for a number
    num = int(input("Enter a number: "))
    
    # Call the subtract_seven function
    result = subtract_seven(num)
    
    # Print the result
    print("Result after subtracting 7:", result)

# This provided line is required at the end of the Python file to call the main() function
if __name__ == '__main__':
    main()
