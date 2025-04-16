import random

# List of country names
words = ["america", "canada", "france", "germany", "pakistan", "australia", "japan", "italy"]

# Random word choice
word = random.choice(words)
guessed_word = "_" * len(word)
attempts = 5

print("Welcome to Hangman!")
print("Guess the country name:", guessed_word)

while attempts > 0:
    guess = input(f"\nYou have {attempts} attempts left. Guess a letter: ").lower()

    if guess.isalpha() and len(guess) == 1:  # Check if input is valid
        if guess in word:
            guessed_word = "".join([guess if word[i] == guess else guessed_word[i] for i in range(len(word))])
            print(f"Good guess! Current word: {guessed_word}")
        else:
            attempts -= 1
            print(f"Wrong guess. {attempts} attempts left.")
    else:
        print("Please enter only one letter.")

    if "_" not in guessed_word:  # Check if the word is fully guessed
        print("Congratulations! You've guessed the country:", word)
        break

if attempts == 0:
    print(f"Game over! The country was: {word}")

