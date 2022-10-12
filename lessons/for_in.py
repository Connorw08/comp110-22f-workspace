"""An example of for in syntax."""

names: list[str] = ["Connor", "Kaki", "Ezri", "Marc"]

# Example of iterating through names using a while loop
print("While output")
i: int = 0
while i < len(names):
    name: str = names[i]
    print(name)
    i += 1

# The following for..in loop is the same as the while loop above
print("for..in output:")
for name in names:
    print(name)

# Sum function rewritten as for..in see sum file for original while loop
def sum(xs: list[float]) -> float:
    """Compute the sum of a list."""
    total: float = 0.0
    for x in xs:
        total += x
    return total