# Helper function to greet the user
def greet(name):
    print(f"Greetings {name}!")

def main():
    # Ask the user for their name
    name = input("What's your name? ")
    
    # Call the greet function with the provided name
    greet(name)

# This provided line is required at the end of Python file to call the main() function
if __name__ == '__main__':
    main()
