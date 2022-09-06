"""One shot wordle!"""

__author__ = "730580207"

secret_word: str = "python"
user_guess: str = input("What is your 6-letter guess? ")
i: int = 0
guess_checker: str = ""
correct_letter: bool = False
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(user_guess) != len(secret_word):  # Checks to see if the length of the user guess is the same as the length as the secret word
    user_guess = input("That was not 6 letters! Try again: ")  # If the lengths aren't the same, user will be asked to input new word

while i < 6:  # Beginning of the while loop that checks every letter for correct letter spots, correct letters but wrong spot, and incorrect letters
    alt_i = 0  # Resets alternate index
    correct_letter = False  # Resets boolean for the correct letter, but wrong spot loop
    
    if secret_word[i] == user_guess[i]:  # If the current letter index of the guess matches the index of the secret word:
        guess_checker += GREEN_BOX  # Then, add a green box to the spot being tested
    elif secret_word[i] != user_guess[i]:  # Else, if the current letter index doesn't match the index of the secret word:
        
        while not correct_letter and alt_i < len(secret_word):  # While there's no current letter match in any position of secret word and alt index < secret word length:
            if user_guess[i] == secret_word[alt_i]:  # If the current letter index of user guess matches the current alt index: 
                correct_letter = True  # Change boolean to True of variable correct_letter, meaning the letter exists somewhere else in word
            elif user_guess[i] != secret_word[alt_i]:  # If the current letter index of user guess matches the current alt index of secret word:
                alt_i += 1  # Increase alt index by 1
        
        if correct_letter is True:  # If letter exists somewhere else in word:
            guess_checker += YELLOW_BOX  # Add a yellow box to current index 
        elif correct_letter is False:  # If letter doesn't exist somewhere else in word:
            guess_checker += WHITE_BOX  # Add a white box to current index! 

    i += 1  # Increase current letter index by 1

if user_guess != secret_word:  # If user guess doesn't match secret word:
    print(guess_checker)  # Prints out boxes, showing incorrect letters (red boxes), letters in the wrong spot (yellow boxes), and correct letters (green boxes)
    print("Not quite. Play again soon!") 
elif user_guess == secret_word:  # If user guess match secret word:
    print(guess_checker)  # Prints out all green boxes since guess is correct
    print("Woo! You got it!") 
