# 02_e=mc2.md
# Constant speed of light (in meters per second)
C = 299792458

def main():
    while True:
        try:
            # Get mass input from user with bold italic prompt
            mass = float(input("\033[1;3mEnter kilos of mass: \033[0m"))

            print("\ne = m * C^2...\n")  # Show the formula

            print(f"m = {mass} kg")       # Show mass
            print(f"C = {C} m/s")         # Show speed of light

            # Calculate energy using Einstein's formula
            energy = mass * C**2

            print(f"\n{energy} joules of energy!\n")  # Display energy result

        except ValueError:
            print("Please enter a valid number for mass.\n")

if __name__ == "__main__":
    main()