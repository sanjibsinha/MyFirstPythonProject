def square(x):
    """
    This module contains a function to calculate the square of a number and a loop to print the squares of a list of numbers.
    Functions:
        square(x): Returns the square of a number.
    Variables:
        numbers (list): A list of numbers to be squared.
    Example:
        The script will print the square of each number in the list `numbers`:
        The square of 1 is 1
        The square of 2 is 4
        The square of 3 is 9
        The square of 4 is 16
        The square of 5 is 25
    """
    """Return the square of a number."""

    return x * x

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    squared_num = square(num)
    print(f"The square of {num} is {squared_num}")

