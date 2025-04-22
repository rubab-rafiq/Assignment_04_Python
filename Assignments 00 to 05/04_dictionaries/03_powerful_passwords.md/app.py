import hashlib  # Module that provides secure hashing functions like SHA-256

# Function to hash the password using SHA-256
def hash_password(password):
    # Convert the password to bytes and return the hexadecimal hash
    return hashlib.sha256(password.encode()).hexdigest()

# Dictionary storing email as key and hashed password as value
stored_logins = {
    "user@example.com": hash_password("password123"),
    "admin@example.com": hash_password("passwordxyz"),
}

# Login function that checks if the hashed password matches the stored hash
def login(email, password_to_check, stored_logins):
    # If email not found, return False
    if email not in stored_logins:
        return False

    # Hash the entered password
    hashed_password = hash_password(password_to_check)

    # Compare with stored hash
    return hashed_password == stored_logins[email]

# --- Main program starts here ---
print("Welcome to Secure Login System")

# Get user input
email = input("Enter your Email: ")
password = input("Enter your Password: ")

# Check login
if login(email, password, stored_logins):
    print("Login Successful! Welcome back.")
else:
    print("Invalid Email or Password. Please try again.")
