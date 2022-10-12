"""Real wordle!!"""

__author__ = "730580207"


def contains_char(word: str, letter: str) -> bool:
    """Returns a bool True or False depending if a single character is found in the first string parameter."""
    assert len(letter) == 1
    correct_letter: bool = False
    i: int = 0
    while not correct_letter and i < len(word):
        if word[i] == letter:
            correct_letter = True
        elif word[i] != letter:
            i += 1
    return correct_letter


def emojified(guess: str, secret: str) -> str:
    """Given two strings of equal length, return a string containing codifying wordle emojis."""
    assert len(guess) == len(secret)
    i: int = 0

    guess_checker: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"

    while i < len(secret):
        if contains_char(secret, guess[i]) is True:
            if guess[i] == secret[i]:
                guess_checker += GREEN_BOX
            elif guess[i] != secret[i]:
                guess_checker += YELLOW_BOX
        else:
            guess_checker += WHITE_BOX
        i += 1
    return guess_checker


def input_guess(length: int) -> str:
    """Given an expected length of a guess, prompts user to give a guess of the correct length."""
    user_guess: str = input(f"Enter a {length} character word: ")
    while len(user_guess) != length:
        user_guess = input(f"That wasn't {length} chars! Try again: ")
    return user_guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word = "codes"
    i = 0

    while i < 6:
        i += 1
        print(f"=== Turn {i}/6 ===")
        user_guess = input_guess(len(secret_word))
        print(emojified(user_guess, secret_word))
        if user_guess == secret_word:
            print(f"You won in {i}/6 turns!")
            i += 7
    if user_guess != secret_word:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()
