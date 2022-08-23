"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730590207"

user_word: str = input("Enter a 5-character word: ")
user_character: str = input("Enter a single character: ")
character_count: int = 0

if len(user_word) > 5:
    print("Error: Word must contain 5 characters")
    quit()
if len(user_character) > 1:
    print("Error: Character must be a single character.")
    quit()


print("Searching for " + user_character + " in " + user_word)

if user_word[0] == user_character:
    print(user_character + " Found at index 0")
    character_count = character_count + 1
if user_word[1] == user_character:
    print(user_character + " found at index 1")
    character_count = character_count + 1
if user_word[2] == user_character:
    print(user_character + " found at index 2")
    character_count = character_count + 1
if user_word[3] == user_character:
    print(user_character + " found at index 3")
    character_count = character_count + 1
if user_word[4] == user_character:
    print(user_character + " found at index 4")
    character_count = character_count + 1

if character_count == 0:
    print("No instances of " + user_character + " found in " + user_word)
if character_count == 1:
    print("1 instance of " + user_character + " found in " + user_word)
if character_count == 2:
    print("2 instances of " + user_character + " found in " + user_word)
if character_count == 3:
    print("3 instances of " + user_character + " found in " + user_word)
if character_count == 4:
    print("4 instances of " + user_character + " found in " + user_word)
if character_count == 5:
    print("5 instances of " + user_character + " found in " + user_word)