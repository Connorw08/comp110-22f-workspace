"""Some unit tests for dictionaries."""

__author__ = "730590207"

from exercises.ex07.dictionary import invert, favorite_color, count


def test_invert_empty() -> None:
    """Test invert function with an empty list."""
    x: dict[str, str] = dict()
    assert invert(x) == {}


def test_invert_one_item() -> None:
    """Test invert function with one item."""
    fruit: dict[str, str] = {"Apple": "Yummy"}
    assert invert(fruit) == {"Yummy": "Apple"}


def test_invert_many_items() -> None:
    """Test invert function with many items."""
    fruit: dict[str, str] = {"Apple": "Yummy", "Pears": "Gross", "Bananas": "Good", "Strawberry": "Okay"}
    assert invert(fruit) == {"Yummy": "Apple", "Gross": "Pears", "Good": "Bananas", "Okay": "Strawberry"}


def test_favorite_color_empty() -> None:
    """Test favorite_color function with an empty list."""
    x: dict[str, str] = dict()
    assert favorite_color(x) == ""


def test_favorite_color_one_item() -> None:
    """Test favorite_color function with one item."""
    x: dict[str, str] = {"Connor": "blue"}
    assert favorite_color(x) == "blue"


def test_favorite_color_many_items() -> None:
    """Test favorite_color function with many items."""
    x: dict[str, str] = {"Connor": "blue", "Ethan": "green", "Kris": "green", "Kyle": "red"}
    assert favorite_color(x) == "green"


def test_count_empty() -> None:
    """Test count function with an empty list."""
    x: list[str] = []
    assert count(x) == {}


def test_count_one_item() -> None:
    """Test count function with one item."""
    fruit: list[str] = ["Apple"]
    assert count(fruit) == {"Apple": 1}


def test_count_many_items() -> None:
    """Test count function with many items."""
    fruit: list[str] = ["Apple", "Banana", "Banana", "Pear", "Banana", "Apple"]
    assert count(fruit) == {"Apple": 2, "Banana": 3, "Pear": 1}