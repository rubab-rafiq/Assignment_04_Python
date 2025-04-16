# Mad Libs Game in Python
import time

print("🌟 Welcome to the Mad Libs Game! 🌟\n")
print("Fill in the blanks to create your own funny story.\n")

# Get user input
name = input("Enter a name: ").capitalize()
place = input("Enter a place: ").capitalize()
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb (past tense): ")
emotion = input("Enter an emotion: ")

# Loading effect (optional)
print("\nGenerating your story...")
time.sleep(2)

# Create the story
#  f-string is used here:
# f""" ... {variable} ... """ means this is a formatted string,
# where the value of the variable inside {} is automatically inserted into the string.

story = f"""
 Here's your Mad Libs story:

One day, {name} went to {place}. It was a very {adjective} day.
Suddenly, they saw a {noun} in the middle of the road.
Without thinking, {name} {verb} towards it.
Everyone was feeling very {emotion} after that!
"""

# Show the story
print(story)