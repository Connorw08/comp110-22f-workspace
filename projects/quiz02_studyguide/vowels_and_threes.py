"""Vowels and threes."""

def vowels_and_threes(user_input: str) -> str:
    """Given a string, return a new string containing an index that is a multiple of 3 or a vowel, but not both."""
    result: str = ""
    i: int = 0
    while i < len(user_input):
        if (i % 3 == 0) and (user_input[i] == "a" or user_input[i] == "i" or user_input == "e" or user_input == "o" or user_input == "u"):
            i += 1
        elif (i % 3 == 0) or (user_input[i] == "a" or user_input[i] == "i" or user_input == "e" or user_input == "o" or user_input == "u"):
            result += user_input[i]
    return result