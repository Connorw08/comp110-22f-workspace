"""List utils."""

__author__ = "730590207"


def only_evens(x: list[int]) -> list[int]:
    """Given a list of ints, return list of only even ints."""
    i = 0
    y: list[int] = list()
    while i < len(x):
        if x[i] % 2 == 0:
            y.append(x[i])
        i += 1
    return y


def concat(a: list[int], b: list[int]) -> list[int]:
    """Given two lists of ints, generate a list that includes all ints in first list followed by ints in second list."""
    new_list: list[int] = list()
    i = 0
    while i < len(a):
        new_list.append(a[i])
        i += 1
    i = 0
    while i < len(b):
        new_list.append(b[i])
        i += 1
    return new_list


def sub(main_list: list[int], start_ix: int, end_ix: int) -> list[int]:
    """Given a list, start index, and end index, return subset of list based off of given start and end."""
    new_list: list[int] = list()
    end_ix -= 1
    if len(main_list) == 0:
        return new_list 
    if start_ix == len(main_list):
        return new_list
    if start_ix < 0:
        start_ix = 0
    if end_ix > len(main_list):
        end_ix = len(main_list) - 1
    new_list.append(main_list[start_ix])
    new_list.append(main_list[end_ix])
    return new_list