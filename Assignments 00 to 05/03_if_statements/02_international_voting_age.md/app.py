# 02_international_voting_age.md
# Function to check if user can vote in the given countries
def check_voting_eligibility(age):
    # Checking for Peturksbouipo, where voting age is 16
    if age >= 16:
        print(f"You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print(f"You cannot vote in Peturksbouipo where the voting age is 16.")
    
    # Checking for Stanlau, where voting age is 25
    if age >= 25:
        print(f"You can vote in Stanlau where the voting age is 25.")
    else:
        print(f"You cannot vote in Stanlau where the voting age is 25.")
    
    # Checking for Mayengua, where voting age is 48
    if age >= 48:
        print(f"You can vote in Mayengua where the voting age is 48.")
    else:
        print(f"You cannot vote in Mayengua where the voting age is 48.")

# Main function to get user's age and call check_voting_eligibility
def main():
    # Ask user for their age
    age = int(input("How old are you? "))  # Convert user input to an integer
    
    # Call the function to check if the user can vote in any country
    check_voting_eligibility(age)

# Entry point of the program
if __name__ == "__main__":
    main()
