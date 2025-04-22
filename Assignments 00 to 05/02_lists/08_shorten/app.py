# Set the maximum number of items allowed in the list
MAX_LENGTH = 3

# This function removes items from the end of the list
# until the list has only MAX_LENGTH items
def shorten(lst):
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()  # Remove the last item from the list
        print(removed)       # Print the removed item

# This is the main function
def main():
    # Ask the user to enter items separated by spaces
    items = input("Enter a list of items separated by spaces: ").split()
    
    # Call the function to shorten the list
    shorten(items)

    # Print the final list after shortening
    print("Shortened list:", items)

# This makes sure the program runs only when this file is run directly
if __name__ == "__main__":
    main()

