INCHES_IN_FOOT: int = 12

def main():
    # Ask the user to enter a length in feet (bold italic prompt)
    feet = float(input("\033[1;3mEnter length in feet: \033[0m"))

    # Convert feet to inches (1 foot = 12 inches)
    inches = feet * INCHES_IN_FOOT

    # Display the result
    print(f"\n{feet} feet is equal to {inches} inches.")

# Run the program
if __name__ == "__main__":
    main()
