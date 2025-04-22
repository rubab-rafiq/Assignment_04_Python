# Function to get user data
def get_user_data():
    # Ask the user for their first name, last name, and email
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")

    # Return all three pieces of data as a tuple
    return first_name, last_name, email

def main():
    # Call the get_user_data function and store the returned values
    user_data = get_user_data()

    # Print the received user data
    print(f"Received the following user data: {user_data}")

# This provided line is required at the end of Python file to call the main() function
if __name__ == '__main__':
    main()
