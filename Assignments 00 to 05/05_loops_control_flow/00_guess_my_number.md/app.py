# 00_guess_my_number.md
import random  # To generate a random number

# Define the main game function
def main():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)

    print("I am thinking of a number between 0 and 99...")

    # Loop until the user guesses the correct number
    while True:
        # Get user's guess and convert to integer
        guess = int(input("Enter a guess: "))

        # Compare guess with the secret number
        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # End the loop when guessed correctly

# Entry point check
if __name__ == '__main__':
    main()
