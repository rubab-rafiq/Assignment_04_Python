# 05_triangle_perimeter.md
def main():
    # Get the lengths of the three sides with bold italic prompts
    side1 = float(input("\033[1;3mEnter the length of side 1: \033[0m"))
    side2 = float(input("\033[1;3mEnter the length of side 2: \033[0m"))
    side3 = float(input("\033[1;3mEnter the length of side 3: \033[0m"))

    # Calculate the perimeter of the triangle
    perimeter = side1 + side2 + side3

    # Print the perimeter result normally
    print(f"The perimeter of the triangle is {perimeter}")

# Run the main function
if __name__ == '__main__':
    main()