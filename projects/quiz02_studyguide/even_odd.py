"""Even and odd code writing problem."""

def odd_and_even(list_1: list[int]) -> list[int]:
    """Yes."""
    new_list: list[int] = []
    i: int = 0
    while i < len(list_1):
        if not(list_1[i] % 2 == 0) and (i % 2 == 0):
            new_list.append(list_1[i])
        i += 1
    
    return new_list


cool: list[int] = [3, 7, 2, 6, 1]


print(odd_and_even(cool))