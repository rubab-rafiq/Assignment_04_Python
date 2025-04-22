# 04_pythagorean_theorem.md
import math 
def main():
    
    ab: float = float(input("\033[1;3mEnter the length of side AB: \033[0m"))
    ac: float = float(input("\033[1;3mEnter the length of side BC: \033[0m"))
    
    # Calculate the length of side AC using the Pythagorean theorem
    bc: float = math.sqrt(ab**2 + ac**2)
    
    # Display the result
    print(f"\nThe length of BC (the hypotenuse): {bc}")

if __name__ == "__main__":
    main()