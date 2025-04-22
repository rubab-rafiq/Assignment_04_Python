# 06_rolldice.md
import random
Num_Sides:int = 6
def main():
    die1:int = random.randint(1, Num_Sides)
    die2:int = random.randint(1, Num_Sides)

    total:int = die1 + die2
    print(f"\nDice have, {Num_Sides} ,sides each.")
    print(f"First Die: {die1}")
    print(f"Second Die: {die2}")
    print(f"Total of two dice: {total}")

if __name__ == "__main__":
    main()