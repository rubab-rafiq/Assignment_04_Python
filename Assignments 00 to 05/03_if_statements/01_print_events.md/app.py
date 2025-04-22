# 01_print_events.md
# This function prints the first 20 even numbers
def main():
    # Loop will run 20 times to get first 20 even numbers
    for i in range(20):
         even_number = i * 2  # Multiply by 2 to get even number
         print(even_number, end=' ')  # Print all on same line with spaces
      
# Call the main function when the file is run directly
if __name__ == "__main__":
    main()
