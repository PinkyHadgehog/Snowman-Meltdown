import random

from ascii_art import STAGES


# List of secret words
WORDS = ["python", "git", "github", "snowman", "meltdown"]


def get_random_word():
    """Selects a random word from the list."""
    return WORDS[random.randint(0, len(WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    """Displays the snowman and the current word state."""

    print(STAGES[mistakes])

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("Word:", display_word)
    print()


def play_game():
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0
    maximum_mistakes = len(STAGES) - 1

    print("Welcome to Snowman Meltdown!")

    while mistakes < maximum_mistakes:
        display_game_state(mistakes, secret_word, guessed_letters)

        guess = input("Guess a letter: ").lower()

        # Only allow one letter
        if len(guess) != 1:
            print("Please enter a single letter.")
            continue

        # Prevent duplicate guesses
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue

        # Correct guess
        if guess in secret_word:
            guessed_letters.append(guess)
            print("Correct guess!")
        else:
            mistakes += 1
            print("Wrong guess!")

        # Check if the whole word has been guessed
        word_is_complete = True

        for letter in secret_word:
            if letter not in guessed_letters:
                word_is_complete = False
                break

        if word_is_complete:
            display_game_state(mistakes, secret_word, guessed_letters)
            print("Congratulations! You saved the snowman!")
            return

    # Game over
    display_game_state(mistakes, secret_word, guessed_letters)
    print("Game over! The snowman melted!")
    print("The secret word was:", secret_word)