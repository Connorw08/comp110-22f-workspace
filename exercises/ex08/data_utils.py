"""Dictionary related utility functions."""

__author__ = "730580207"

from csv import DictReader
# Define your functions below


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepare to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)

    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)

    # Close the file when we're done, to free its resources.
    file_handle.close()

    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}
    
    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)

    return result


def head(data: dict[str, list[str]], n: int) -> dict[str, list[str]]:
    """Creates a new column based table with only the first n rows of data for each column."""
    result: dict[str, list[str]] = {}
    if n > len(data):
        result = data
    else:
        for key in data:
            new: list[str] = []
            for i in range(n):
                new.append(data[key][i])
            result[key] = new
    return result


def select(table: dict[str, list[str]], copy: list[str]) -> dict[str, list[str]]:
    """Creates a new column-based table with only a specified subset of the original columns."""
    result: dict[str, list[str]] = {}
    i: int = 0
    while i < len(copy):
        for key in table:
            if key == copy[i]:
                result[key] = table[key]
        i += 1

    return result


def concat(data_1: dict[str, list[str]], data_2: dict[str, list[str]]) -> dict[str, list[str]]:
    """Creates a new column-based table by combining two column-based tables."""
    result: dict[str, list[str]] = {}
    for key in data_1:
        result[key] = data_1[key]
    for key in data_2:
        if key in result:
            result[key] += data_2[key]
        if key not in result:
            result[key] = data_2[key]

    return result


def count(values: list[str]) -> dict[str, int]:
    """Given a list of str, make a list that counts the number of items."""
    result: dict[str, int] = dict()
    i = 0
    while i < len(values):
        if values[i] in result:
            result[values[i]] += 1
        if values[i] not in result:
            result[values[i]] = 1
        i += 1
    return result