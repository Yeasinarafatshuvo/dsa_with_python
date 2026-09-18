import pytest

from index import linear_search


@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        # Normal case
        ([10, 20, 30, 40, 50], 30, 2),

        # First element
        ([10, 20, 30, 40, 50], 10, 0),

        # Last element
        ([10, 20, 30, 40, 50], 50, 4),

        # Element not found
        ([10, 20, 30, 40, 50], 35, -1),

        # Empty list
        ([], 10, -1),

        # Single element - found
        ([10], 10, 0),

        # Single element - not found
        ([10], 20, -1),

        # Duplicate values - should return first occurrence
        ([10, 20, 30, 20, 50], 20, 1),

        # Negative numbers
        ([-50, -20, -10, 0, 10], -20, 1),

        # Zero
        ([10, 20, 0, 40, 50], 0, 2),
    ]
)

def test_linear_search(numbers, target, expected):
    result = linear_search(numbers, target)
    assert result == expected

