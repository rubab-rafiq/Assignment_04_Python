# 02_agreement_bot.md
def main():
    # Ask the user for their favorite animal using formatted text (italic + bold)
    favorite_animal = input("\033[1;3m What's your favorite animal? \033[0m")

    # Print the response including the user's favorite animal
    print(f"My favorite animal is also {favorite_animal}!")

if __name__ == '__main__':
    main()