# This is the affirmation the user needs to type correctly
affirmation = "I am capable of doing anything I put my mind to."

# Function to ask the user to type the affirmation until it's correct
def main():
    # The program will ask the user to type the affirmation until it's correct
    while True:
        user_input = input("Please type the following affirmation: ")  # Taking input from the user
        
        # If the user types the correct affirmation, the loop will stop
        if user_input == affirmation:
            print("That's right! :)")  # Message shown when the user types it correctly
            break  # Exit the loop
        else:
            print("Hmmm That was not the affirmation.")  # Message shown when the user types it incorrectly

# This block ensures that the main() function is called only when the script is run directly
if __name__ == '__main__':
    main()
