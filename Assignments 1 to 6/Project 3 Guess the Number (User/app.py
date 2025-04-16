import random

# Welcome message
print("🎉 Welcome to the Guess the Number Game!")

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Initialize attempts
attempts = 0

while True:
    # Get user input
    guess = input("Enter your guess (1 to 10): ")

    # Check if input is a number
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    # Convert guess to integer
    guess = int(guess)
    attempts += 1

    # Check the guess
    if guess < secret_number:
        print("Too low! Try again. 🔽")
    elif guess > secret_number:
        print("Too high! Try again. 🔼")
    else:
        print(f"🎉 Congratulations! You guessed the number in {attempts} attempts.")
        break
