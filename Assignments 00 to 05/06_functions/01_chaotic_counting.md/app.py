import random

DONE_LIKELIHOOD = 0.2  # Chance of stopping early

def done():
    # Returns True with a certain probability
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    # Count from 1 to 10, but stop early if done() is True
    for i in range(1, 11):
        if done():  # Check if we should stop
            return  # Exit function if done() is True
        print(i)  # Print the current number
    
def main():
    # Start counting and show message
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()  # Start counting
    print("I'm done.")  # Print once counting is finished

main()
