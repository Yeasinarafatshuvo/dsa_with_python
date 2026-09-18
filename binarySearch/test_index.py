import pytest

from index import binary_search

@pytest.mark.parametrize(
    "numbers, target, expected",
    [
        #normal case
        ([10, 20, 30, 40, 50], 30, 2),

        #frist element
        ([10, 20, 30, 40, 50], 10, 0),

        #last element
        ([10, 20, 30, 40, 50], 50, 4),

        #element not found
        ([10, 20, 30, 40, 50], 35, -1),

        #empty list
        ([], 10, -1),

        #single element found
        ([10], 10, 0),

        #single element not found
        ([10], 20, -1)

    ]
)

def test_bineary_search(numbers, target, expected):
    result = binary_search(numbers, target)
    assert  result == expected
