import pytest

from index import selection_sort


@pytest.mark.parametrize(
    "numbers, expected",
    [
        # Normal unsorted list
        ([64, 25, 12, 22, 11], [11, 12, 22, 25, 64]),

        # Already sorted
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),

        # Reverse sorted
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),

        # Empty list
        ([], []),

        # Single element
        ([10], [10]),

        # Two elements
        ([20, 10], [10, 20]),

        # Duplicate values
        ([5, 2, 8, 2, 1, 5], [1, 2, 2, 5, 5, 8]),

        # Negative numbers
        ([-5, 3, -1, 0, -10], [-10, -5, -1, 0, 3]),

        # All same values
        ([7, 7, 7, 7], [7, 7, 7, 7]),

        # Zero values
        ([0, 5, 2, 0, 1], [0, 0, 1, 2, 5]),
    ]
)

def test_selection_sort(numbers, expected):
    selection_sort(numbers)
    assert numbers == expected

