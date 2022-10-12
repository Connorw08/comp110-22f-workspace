"""Something with lists!"""
__author__ = "730580207"


def all(list: list[int], check_number: int) -> bool:
    """Given a number, check to see if number exists in list and True or False."""
    i = 0
    if len(list) == 0:  # If list is empty, return False.
        return False

    while i < len(list):
        if list[i] != check_number:  # If current index int doesn't equal the check_number, return False.
            return False
        i += 1
    return True
    

def max(list: list[int]) -> int:
    """Given a list of ints, return the largest int."""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    largest_number = list[0]  # Stores the first int as that's the current largest int.

    i = 0
    while i < len(list):
        if list[i] >= largest_number:  # Checks to see if current index is larger than stored int.
            largest_number = list[i]  # If true, becomes largest current int.
        i += 1
    return largest_number


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Given 2 list of ints, check to see if they are equal."""
    if len(list_1) == 0 and len(list_2) == 0:  # If both lists are empty, then return True.
        return True

    if len(list_1) == 0 or len(list_2) == 0:  # Checks if only one list is empty if so, False.
        return False

    if len(list_1) != len(list_2):  # Checks if length of lists are the same, if they aren't, return False.
        return False
    
    i = 0
    while i < len(list_1): 
        if list_1[i] != list_2[i]:  # If current index int doesn't equal current index of other list, return False.
            return False
        i += 1
    return True   