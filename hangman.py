import random

# Load the vocabulary from the file
with open('vocabularies.txt', 'r') as file:
    vocabularies = file.readlines()
    vocabularies = [word.strip().lower() for word in vocabularies]

def choose_word():
    """Choose a random word from the vocabulary list"""
    return random.choice(vocabularies)

def display_word(word, guessed_letters):
    """Display the word with dashes for unguessed letters"""
    displayed_word = ""
    for letter in word:
        if letter in guessed_letters:
            displayed_word += letter
        else:
            displayed_word += "-"
    return displayed_word

def hangman():
    """Main game loop"""
    print("Welcome to Hangman!")
    word = choose_word()
    guessed_letters = []
    attempts = 6

    while True:
        print("\nAttempts remaining:", attempts)
        print("Guessed letters:", guessed_letters)
        print(display_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("Correct guess!")
            if "-" not in display_word(word, guessed_letters):
                print("\nCongratulations! You guessed the word:", word)
                break
        else:
            print("Wrong guess!")
            attempts -= 1

        if attempts == 0:
            print("\nGame over! The word was:", word)
            break

hangman()