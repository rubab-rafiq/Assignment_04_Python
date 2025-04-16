import random  # Used to pick random characters
import string  # Provides letters, digits, and symbols

# Function to create a password
def generate_password(length):
    # All possible characters (letters + numbers + symbols)
    characters = string.ascii_letters + string.digits + string.punctuation

    # Pick random characters and join them into a password
    password = ''.join(random.choice(characters) for i in range(length))

    return password  # Return the final password

# Start of the program
print("Welcome to the Password Generator!")

# Ask user for password length
password_length = int(input("Enter the length of the password: "))

# Generate password using the function
password = generate_password(password_length)

# Show the result
print(f"Your generated password is: {password}")