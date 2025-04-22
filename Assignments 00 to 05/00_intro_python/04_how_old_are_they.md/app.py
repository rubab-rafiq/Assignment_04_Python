# 04_how_old_are_they.md
def main():
   # Anthon's age is fixed at 21
    Anthon_age = 21

    # Beth is 6 years older than Anthon
    Beth_age = Anthon_age + 6

    # Chen is 20 years older than Beth
    Chen_age = Beth_age + 20

    # Drew's age is the sum of Chen's and Anthon's ages
    Drew_age = Chen_age + Anthon_age

    # Enthan's age is the same as Chen's age
    Enthan_age = Chen_age

    # Print the ages of all the individuals
    print(f"Anthon is {Anthon_age} years old.")
    print(f"Beth is {Beth_age} years old.")
    print(f"Chen is {Chen_age} years old.")
    print(f"Drew is {Drew_age} years old.")
    print(f"Enthan is {Enthan_age} years old.")


if __name__ == '__main__':
    main()