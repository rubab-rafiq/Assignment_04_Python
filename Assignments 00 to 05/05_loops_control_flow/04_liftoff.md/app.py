# This is the main function where the countdown and liftoff will happen
def main():
    # This for loop will start from 10 and count down to 1
    for i in range(10, 0, -1):
        print(i, end=" ")  # Print each number in the countdown, separated by space on the same line
    
    # After the countdown is complete, we print "Liftoff!"
    print("Liftoff!")

# This block ensures that the main function runs only if the script is executed directly
if __name__ == '__main__':
    main()  # Calling the main function to execute the program
