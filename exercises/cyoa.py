"""Choose Your Own Adventure program."""

__author__ = "730590207"

from random import randint

points: int
player: str
SHREK: str = "\U0001F49A"
CAT: str = "\U0001F408"
PRINCESS: str = "\U0001F478"
DONKEY: str = "\U0001F40E"


def main() -> None:
    """The entrypoint of the program and main game loop."""
    global player
    playing: bool = True
    greet()
    while playing is True:
        global points
        points = 0
        first_q()
        points = q2(points)
        points = q3(points)
        points = q4(points)
        points += bonus(points)
        playing = end_quiz(points)
    print(f"Thank you for playing {player}! Have a good day!")


def greet() -> None:
    """Greet the user and asking for a str input. Changes "player" variable in global."""
    global player
    # Assign name input by user to global variable named 'player.'
    player = input("Welcome user to What character from Shrek are you? After this quiz, you will learn the valuable knowledge of what character you are from Shrek. \nTo start, what is your name? ")


def first_q() -> None:
    """Q1: Uses the global int points and asks a question to the user. Based on their response, increase points value."""
    global player
    global points

    user_response: int = int(input(f"Q1: {player}, what food would you like to eat? (Type just the number. EX: \"1\")\n1) A delicious cake \n2) Stew \n3) Milk and cookies \n4) Waffles \n"))
    while not (user_response > 0 and user_response < 5):
        user_response = int(input("Try again! Please give a valid response. (Type just the number. EX: \"1\")\n"))
    if user_response == 1:
        points += 1
    if user_response == 2:
        points += 4
    if user_response == 3:
        points += 2
    if user_response == 4:
        points += 3


def q2(points: int) -> int:
    """Q2: Uses a starting point value and asks a question to the user. Based on their response, increase point value."""
    global player
    user_response: int = int(input(f"Q2: {player}, where would you prefer to live? (Type just the number. EX: \"1\")\n1) A castle \n2) Anywhere you're always on the move! \n3)A friend's house \n4) A swamp \n"))
    while not (user_response > 0 and user_response < 5):
        user_response = int(input("Try again! Please give a valid response. (Type just the number. EX: \"1\")\n"))
    if user_response == 1:
        points += 1
    if user_response == 2:
        points += 2
    if user_response == 3:
        points += 3
    if user_response == 4:
        points += 4
    return points


def q3(points: int) -> int:
    """Q3: Uses a starting point value and asks a question to the user. Based on their response, increase point value."""
    global player
    user_response = int(input(f"Q3: {player}, what movie genre is your favorite? (Type just the number. EX: \"1\")\n1) Adventure \n2) Romance \n3) Comedy \n4) Horror \n"))
    while not (user_response > 0 and user_response < 5):
        user_response = int(input("Try again! Please give a valid response. (Type just the number. EX: \"1\")\n"))
    if user_response == 1:
        points += 2
    if user_response == 2:
        points += 1
    if user_response == 3:
        points += 3
    if user_response == 4:
        points += 4
    return points


def q4(points: int) -> int:
    """Q4: Uses a starting point value and asks a question to the user. Based on their response, increase point value."""
    global player
    user_response: int = int(input(f"Q4: {player}, choose a vacation to go on. (Type just the number. EX: \"1\")\n1) I prefer to stay at home \n2) Camping in the Alps \n3) Atlantis in the Bahamas \n4) A trip to the French Riviera \n"))
    while not (user_response > 0 and user_response < 5):
        user_response = int(input("Try again! Please give a valid response. (Type just the number. EX: \"1\")\n"))
    if user_response == 1:
        points += 4
    if user_response == 2:
        points += 2
    if user_response == 3:
        points += 3
    if user_response == 4:
        points += 1
    return points


def bonus(points: int) -> int:  #
    """Generates a random int and adds int to global "points" variable."""
    # Use of randomness.
    global player
    points = randint(1, 4)
    print(f"Congrats {player}! For finishing the quiz you will recieve {points} bonus points!")
    return points


def end_quiz(points: int) -> bool:
    """Based on player's points, print what character they are from Shrek. Returns bool based on if they want to keep playing."""
    global SHREK
    global CAT
    global PRINCESS
    global DONKEY

    if points > 3 and points < 8:
        print(f"You have gathered {points} points! This means you are most like Princess Fiona {PRINCESS}!")
    if points > 7 and points < 11:
        print(f"You have gathered {points} points! This means you are most like Puss in Boots {CAT}!")
    if points > 10 and points < 14:
        print(f"You have gathered {points} points! This means you are most like Donkey {DONKEY}!")
    if points > 13:
        print(f"You have gathered {points} points! This means you are most like Shrek {SHREK}!")
    keep_playing: int = int(input("Would you like to try again? (Type just the number. EX: \"1\")\n1) Yes \n2) No \n"))
    while not (keep_playing > 0 and keep_playing < 3):
        keep_playing = int(input("Try again! Please give a valid response. (Type just the number. EX: \"1\")\n"))
    if keep_playing == 1:
        return True
    return False


if __name__ == "__main__":
    main()