"""Some utils for dictionaries."""

__author__ = "730590207"


def invert(user_dict: dict[str, str]) -> dict[str, str]:
    """Given a dictionary of str, str, return a dictionary that inverts the keys and the values."""
    new_dict: dict[str, str]
    new_dict = dict()

    for key in user_dict:
        if user_dict[key] in new_dict:
            raise KeyError
        new_dict[user_dict[key]] = key

    return new_dict


def favorite_color(user_dict: dict[str, str]) -> str:
    """Given a dictionary of str, str, return the name of the color that appears the most."""
    count_dict: dict[str, int] = dict()
    common_color: str = ""
    max_number: int = 0
    if len(user_dict) == 0:
        return common_color
    for key in user_dict:
        if user_dict[key] in count_dict:
            count_dict[user_dict[key]] += 1
        if user_dict[key] not in count_dict:
            count_dict[user_dict[key]] = 1   
    for key in count_dict:
        if max_number < count_dict[key]:
            max_number = count_dict[key]
            common_color = key
    return common_color


def count(user_list: list[str]) -> dict[str, int]:
    """Given a list of str, make a list that counts the number of items."""
    new_dict: dict[str, int] = dict()
    i = 0
    while i < len(user_list):
        if user_list[i] in new_dict:
            new_dict[user_list[i]] += 1
        if user_list[i] not in new_dict:
            new_dict[user_list[i]] = 1
        i += 1
    return new_dict