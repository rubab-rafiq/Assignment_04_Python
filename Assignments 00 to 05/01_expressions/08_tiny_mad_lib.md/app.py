# 08_tiny_mad_lib.md
# Commit: Add Mad Libs style sentence generator using user inputs

# Constant sentence beginning
SENTENCE_START: str = "With just a few lines of code, I made my"

def main():
    # Ask the user for input words with styled prompts
    adjective = input("\033[1;3mPlease type an adjective and press enter: \033[0m")
    noun = input("\033[1;3mPlease type a noun and press enter: \033[0m")
    verb = input("\033[1;3mPlease type a verb and press enter: \033[0m")
  
    # Create and print the final fun sentence
    print(f"\n{SENTENCE_START} {adjective} {noun} {verb}!")

if __name__ == "__main__":
    main()
