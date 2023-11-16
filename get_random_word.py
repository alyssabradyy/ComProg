print("Welcome to hangman!")

secret_word = with open("randomwordgen.py", "r") as file:
    allText = file.read()
    words = list(map(str, allText.split()))
    code_word = split(secret_word)

print(f"This is your word:{enumerate(code_word)}")
guesses = input("What letter would you like to guess? ")

if guesses == code_word:
    print(f"{guesses in code_word}_ _ _ _ _ _ _ _ _ _ _ _ _")
