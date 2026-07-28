import random

# List of predefined words
words = ["python", "computer", "keyboard", "program", "network"]

# Randomly choose a word
secret_word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
attempts = 6

print("=" * 40)
print("        WELCOME TO HANGMAN")
print("=" * 40)

while attempts > 0:

    # Display current progress
    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if player has guessed the word
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong guess!")
        print("Attempts left:", attempts)

if attempts == 0:
    print("\nGame Over!")
    print("The word was:", secret_word)
