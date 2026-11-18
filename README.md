# CodeAlpha_HangmanGame

**CodeAlpha Task 1 - Hangman Game**

A text-only Python Hangman game. A random word is selected from **exactly five predefined words**, and the player guesses **one letter at a time**, with **six incorrect guesses** allowed. No files, web requests, third-party libraries, or graphics are used.

## Run

```bash
python main.py
```

On Windows, `py main.py` also works. Python 3.9+ is recommended.

## How to play

1. Enter one English letter per turn.
2. Correct guesses reveal matching letters in the word.
3. Incorrect guesses consume one of six attempts.
4. Repeated guesses and invalid entries do not use an attempt.
5. Reveal all letters to win, or reach six incorrect guesses to lose.

## Example

```text
=== CODEALPHA HANGMAN GAME ===
Guess the hidden word! You can make 6 incorrect guesses.

Word: _ _ _ _ _ _
Incorrect guesses: 0/6
Letters tried: None
Enter one letter: p
Correct guess!
```

## Test

```bash
python -m unittest discover -s tests -v
```

**Key concepts:** `random`, `while`, `if`/`else`, strings, lists, sets, console input/output.

**Source:** `main.py`.
