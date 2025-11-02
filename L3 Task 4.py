from typing import Iterable, Union

Number = Union[int, float]

def sum_of_squares(numbers: Iterable[Number]) -> Number:
    """
    Return the sum of squares of the given numbers.

    Args:
        numbers: An iterable of numbers (ints or floats).

    Returns:
        The sum of x*x for each x in numbers.

    Examples:
        >>> sum_of_squares([1, 2, 3])
        14
    """
    total: Number = 0
    for x in numbers:
        total += x * x
    return total

if __name__ == "__main__":
    # Example 1: list input
    data = [1, 2, 3, 4]
    print("Input list:", data)
    print("Sum of squares:", sum_of_squares(data))  # 1+4+9+16 = 30

    # Example 2: generator input (lazy iterable)
    gen = (i for i in range(1, 6))  # 1..5 => 1+4+9+16+25 = 55
    print("Input generator: range(1,6)")
    print("Sum of squares:", sum_of_squares(gen))

    # Basic assertions (simple tests)
    assert sum_of_squares([0]) == 0
    assert sum_of_squares([-1, 1]) == 2
    assert sum_of_squares([]) == 0

    print("All basic checks passed.")