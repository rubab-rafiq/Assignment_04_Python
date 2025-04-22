# Maximum value set for Fibonacci terms
MAX_TERM_VALUE : int = 10000

def main():
    # Starting the first two Fibonacci numbers
    curr_term = 0  # First term
    next_term = 1  # Second term
    
    # Keep generating terms until current term is less than or equal to MAX_TERM_VALUE
    while curr_term <= MAX_TERM_VALUE:
        print(curr_term)  # Print the current Fibonacci term
        
        # Calculate the next term in the Fibonacci sequence
        term_after_next = curr_term + next_term
        
        # Update the current and next terms for the next iteration
        curr_term = next_term
        next_term = term_after_next  # Update to the next Fibonacci number

# If this file is being run directly, call the main function
if __name__ == '__main__':
    main()
