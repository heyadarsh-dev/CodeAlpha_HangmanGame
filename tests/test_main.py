"""Unit tests for the Hangman game."""

import unittest
from main import MAX_INCORRECT_GUESSES, WORDS, display_word, play_game


class HangmanTests(unittest.TestCase):
    def test_five_predefined_words(self):
        self.assertEqual(len(WORDS), 5)
        self.assertEqual(len(set(WORDS)), 5)

    def test_hide_and_reveal_letters(self):
        self.assertEqual(display_word("python", {"p", "o"}), "p _ _ _ o _")

    def test_player_wins(self):
        answers = iter("python")
        messages = []
        self.assertTrue(play_game("python", lambda _: next(answers), messages.append))
        self.assertTrue(any("Congratulations" in msg for msg in messages))

    def test_player_loses_after_six_wrong_guesses(self):
        answers = iter("abcdef")
        messages = []
        self.assertFalse(play_game("python", lambda _: next(answers), messages.append))
        self.assertTrue(any("Game over" in msg for msg in messages))
        self.assertEqual(MAX_INCORRECT_GUESSES, 6)

    def test_duplicate_and_invalid_guesses_do_not_consume_attempts(self):
        answers = iter(["!", "zz", "a", "a", "b", "c", "d", "e", "f"])
        messages = []
        self.assertFalse(play_game("python", lambda _: next(answers), messages.append))
        self.assertTrue(any("already guessed" in msg for msg in messages))
        self.assertTrue(any("Invalid input" in msg for msg in messages))

    def test_invalid_secret_word(self):
        with self.assertRaises(ValueError):
            play_game("hello world")


if __name__ == "__main__":
    unittest.main()
