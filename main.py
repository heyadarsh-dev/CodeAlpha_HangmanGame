"""Text-based Hangman game for the CodeAlpha Python internship."""

import random

WORDS = ["python", "computer", "keyboard", "program", "developer"]
MAX_INCORRECT_GUESSES = 6


def display_word(word, guessed_letters):
    """Return the word with unguessed letters hidden."""
    return " ".join(letter if letter in guessed_letters else "_" for letter in word)


def play_game(word=None, input_fn=input, output_fn=print):
    """Play one Hangman round. Return True when the player wins."""
    secret_word = word if word is not None else random.choice(WORDS)
    if not secret_word or not secret_word.isascii() or not secret_word.isalpha():
        raise ValueError("The secret word must contain English letters only.")
    secret_word = secret_word.lower()

    guessed_letters = set()
    incorrect_guesses = 0

    output_fn("=== CODEALPHA HANGMAN GAME ===")
    output_fn(f"Guess the hidden word! You can make {MAX_INCORRECT_GUESSES} incorrect guesses.")

    while incorrect_guesses < MAX_INCORRECT_GUESSES:
        output_fn(f"\nWord: {display_word(secret_word, guessed_letters)}")
        output_fn(f"Incorrect guesses: {incorrect_guesses}/{MAX_INCORRECT_GUESSES}")
        output_fn("Letters tried: " + (", ".join(sorted(guessed_letters)) or "None"))

        if all(letter in guessed_letters for letter in secret_word):
            output_fn(f"Congratulations! You guessed '{secret_word}'.")
            return True

        guess = input_fn("Enter one letter: ").strip().lower()
        if len(guess) != 1 or not guess.isascii() or not guess.isalpha():
            output_fn("Invalid input. Enter exactly one English letter (A-Z).")
            continue
        if guess in guessed_letters:
            output_fn("You already guessed that letter. Try another.")
            continue

        guessed_letters.add(guess)
        if guess in secret_word:
            output_fn("Correct guess!")
        else:
            incorrect_guesses += 1
            output_fn("Incorrect guess!")

    output_fn(f"\nGame over! The word was '{secret_word}'.")
    return False


if __name__ == "__main__":
    play_game()
