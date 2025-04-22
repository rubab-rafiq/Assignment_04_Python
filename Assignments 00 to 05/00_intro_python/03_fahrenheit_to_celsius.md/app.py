# 03_fahrenheit_to_celsius.md
def main():
    # Ask the user to input temperature in Fahrenheit
    degrees_fahrenheit = float(input("\033[1;3m Enter temperature in Fahrenheit: \033[0m"))

    # Convert Fahrenheit to Celsius using the formula
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0

    # Print the result with proper formatting
    print(f"Temperature: {degrees_fahrenheit}F = {degrees_celsius}C")

# Run the main function if this script is executed directly
if __name__ == '__main__':
    main()
