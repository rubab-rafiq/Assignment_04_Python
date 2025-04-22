# Initialize an empty dictionary to store the phonebook data
phonebook = {}

# Loop to add contacts to the phonebook
while True:
    # Get the name of the contact from the user
    user_name = input("Name: ")
    # If the user enters an empty string, break the loop (stop adding contacts)
    if user_name == "":
        break
    # Get the phone number for the contact
    number = input("Number: ")
    # Add the contact (name and number) to the phonebook dictionary
    phonebook[user_name] = number

# Function to print all contacts in the phonebook
def print_phonebook(phonebook):
    # Loop through each name in the phonebook
    for name in phonebook:
        # Print the name and corresponding phone number
        print(str(name) + " -> " + str(phonebook[name]))

# Loop to allow the user to search for contacts by name
while True:
    # Ask the user to enter a name to look up
    name = input("Enter name to lookup: ")
    # If the user enters an empty string, break the loop (stop searching)
    if name == "":
        break
    # Check if the entered name exists in the phonebook
    if name not in phonebook:
        # If the name is not found, inform the user
        print(name + " is not in the phonebook")
    else:
        # If the name is found, display the corresponding phone number
        print(phonebook[name])
