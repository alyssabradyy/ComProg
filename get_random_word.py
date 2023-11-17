print("Welcome to hangman!")

secret_word = "autobiography"

print("This is your word:_ _ _ _ _ _ _ _ _ _ _ _ _")
guesses = input("What letter would you like to guess? ")
if guesses == split(secret_word):
    print(f"{guesses in secret_word}_ _ _ _ _ _ _ _ _ _ _ _ _")
