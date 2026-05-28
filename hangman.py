# ============================================
#   HANGMAN GAME — CodeAlpha Internship Task 1
#   Author: Intern
# ============================================

import random

# ── 5 predefined words ──────────────────────
WORDS = ["python", "rocket", "mango", "bridge", "planet"]

# ── Hangman ASCII art (0 to 6 wrong guesses) ─
HANGMAN_STAGES = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\\  |
      / \\  |
           |
    =========
    """,
]

def display_word(secret_word, guessed_letters):
    """Show the word with blanks for unguessed letters."""
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter + " "
        else:
            display += "_ "
    return display.strip()

def play_hangman():
    secret_word = random.choice(WORDS)
    guessed_letters = set()
    wrong_guesses   = 0
    max_wrong       = 6

    print("\n" + "=" * 40)
    print("       Welcome to HANGMAN GAME!")
    print("=" * 40)
    print(f"The word has {len(secret_word)} letters. Good luck!\n")

    while wrong_guesses < max_wrong:
        # Show current hangman stage
        print(HANGMAN_STAGES[wrong_guesses])

        # Show word progress
        print("Word:  ", display_word(secret_word, guessed_letters))
        print(f"Wrong guesses left: {max_wrong - wrong_guesses}")

        if guessed_letters:
            print("Letters guessed:", ", ".join(sorted(guessed_letters)))

        # Get player input
        guess = input("\nGuess a letter: ").lower().strip()

        # Validate input
        if len(guess) != 1 or not guess.isalpha():
            print("⚠  Please enter a single letter!")
            continue

        if guess in guessed_letters:
            print(f"⚠  You already guessed '{guess}'. Try another!")
            continue

        guessed_letters.add(guess)

        if guess in secret_word:
            print(f"✅  Great! '{guess}' is in the word!")
        else:
            wrong_guesses += 1
            print(f"❌  '{guess}' is NOT in the word!")

        # Check win condition
        if all(letter in guessed_letters for letter in secret_word):
            print(HANGMAN_STAGES[wrong_guesses])
            print("\n🎉 CONGRATULATIONS! You guessed the word:", secret_word.upper())
            break
    else:
        # Player lost
        print(HANGMAN_STAGES[max_wrong])
        print(f"\n💀 GAME OVER! The word was: {secret_word.upper()}")

    # Play again?
    again = input("\nPlay again? (yes / no): ").lower().strip()
    if again in ("yes", "y"):
        play_hangman()
    else:
        print("\nThanks for playing! Goodbye 👋\n")

# ── Entry point ──────────────────────────────
if __name__ == "__main__":
    play_hangman()
