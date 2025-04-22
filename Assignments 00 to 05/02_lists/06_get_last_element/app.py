def get_first_element(lst):
    # Print the first element of the list
    print("First element:", lst[-1])

def main():
    # Ask how many elements the user wants to enter
    n = int(input("How many elements will be in the list? "))

    # Create an empty list
    lst = []

    # Get elements from the user one by one
    for i in range(n):
        item = input(f"Enter element {i+1}: ")
        lst.append(item)

    # Call the function to print the first element
    get_first_element(lst)

# Run the program
if __name__ == "__main__":
    main()

