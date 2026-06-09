import pytest

from exercises import control_flow as ex


@pytest.mark.parametrize(
    "s, expected",
    [
        ("A man, a plan, a canal: Panama", True),
        ("hello", False),
        ("Racecar", True),
        ("", True),
        ("a", True),
    ],
)
def test_is_palindrome(s, expected):
    assert ex.is_palindrome(s) == expected


def test_fizzbuzz():
    assert ex.fizzbuzz(15) == [
        "1",
        "2",
        "Fizz",
        "4",
        "Buzz",
        "Fizz",
        "7",
        "8",
        "Fizz",
        "Buzz",
        "11",
        "Fizz",
        "13",
        "14",
        "FizzBuzz",
    ]


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, 2, 4], 2),
        ([1, 2, 3], None),
        ([5, 5], 5),
        ([], None),
    ],
)
def test_find_first_duplicate(nums, expected):
    assert ex.find_first_duplicate(nums) == expected


@pytest.mark.parametrize(
    "nums, expected",
    [
        ([1, 2, 3, -1, 10], 6),
        ([5, 5, 5], 15),
        ([-1], 0),
        ([], 0),
    ],
)
def test_sum_until_negative(nums, expected):
    assert ex.sum_until_negative(nums) == expected
