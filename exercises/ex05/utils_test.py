"""Test util lists."""

__author__ = "730590207"


from exercises.ex05.utils import only_evens, concat, sub


def test_only_evens_empty() -> None:
    """Test only_evens function with an empty list."""
    x: list[int] = ()
    assert only_evens(x) == []


def test_only_evens_one_item() -> None:
    """Test only_evens function with one int."""
    x: list[int] = [2]
    assert only_evens(x) == [2]


def test_only_evens_many_items() -> None:
    """Test only_evens function with many ints."""
    x: list[int] = [4, 3, 7, 6, 8]
    assert only_evens(x) == [4, 6, 8]


def test_concat_empty_list() -> None:
    """Test concat function with empty list."""
    x: list[int] = []
    y: list[int] = []
    assert concat(x, y) == []


def test_concat_one_item() -> None:
    """Test concat function with one int."""
    x: list[int] = [1]
    y: list[int] = [2]
    assert concat(x, y) == [1, 2]


def test_concat_many_items() -> None:
    """Test concat function with many ints."""
    x: list[int] = [1, 2, 3]
    y: list[int] = [4, 5, 6]
    assert concat(x, y) == [1, 2, 3, 4, 5, 6]


def test_sub_empty() -> None:
    """Test sub function with an empty list."""
    x: list[int] = []
    y = 2
    z = 3
    assert sub(x, y, z) == []


def test_sub_one_item() -> None:
    """Test sub function with one int."""
    x: list[int] = [5]
    y = 0
    z = 0
    assert sub(x, y, z) == [5, 5]


def test_sub_many_items() -> None:
    """Test sub function with many items."""
    x: list[int] = [10, 20, 30, 40]
    y = 1
    z = 3
    assert sub(x, y, z) == [20, 30]