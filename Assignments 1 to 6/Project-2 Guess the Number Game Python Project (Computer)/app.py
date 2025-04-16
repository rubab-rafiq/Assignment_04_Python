import random

print("Think of a number between 1 and 10.")
print("I will try to guess it!")

low = 1
high = 10
attempts = 0

while True:
    if low > high:
        print("Something went wrong. Did you give the correct hints?")
        break

    guess = random.randint(low, high)
    attempts += 1


    print(f"\nIs your number {guess}?")
    feedback = input("Enter 'h' if too high, 'l' if too low, or 'c' if correct: ").lower()

    if feedback == 'h':
        high = guess - 1
    elif feedback == 'l':
        low = guess + 1
    elif feedback == 'c':
        print(f"\nI guessed your number in {attempts} attempts!")
        break
    else:
        print("Invalid input. Please enter 'h', 'l', or 'c'.")


