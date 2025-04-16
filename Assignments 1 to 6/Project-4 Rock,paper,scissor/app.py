import random

options = ["rock", "paper", "scissors"]

print("Let's play Rock, Paper, Scissors!")

while True:
    user = input("Choose rock, paper, or scissors (or 'q' to quit): ").lower()

    if user == 'q':
        print("Game over. Thanks for playing!")
        break

    if user not in options:
        print("Invalid choice. Try again.")
        continue

    computer = random.choice(options)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")