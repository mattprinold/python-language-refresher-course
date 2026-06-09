"""Exercise 2: Control flow — conditionals and loops."""


def is_palindrome(s: str) -> bool:
    """Return True if `s` is a palindrome, ignoring case and non-alphanumeric chars.

    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("hello")
    False
    """
    raise NotImplementedError


def fizzbuzz(n: int) -> list[str]:
    """Return a list of FizzBuzz values for integers 1 through `n` (inclusive).

    Multiples of 3 -> "Fizz", multiples of 5 -> "Buzz", both -> "FizzBuzz",
    otherwise the number as a string.

    >>> fizzbuzz(5)
    ['1', '2', 'Fizz', '4', 'Buzz']
    """
    raise NotImplementedError


def find_first_duplicate(nums: list[int]) -> int | None:
    """Return the first value that appears more than once, or None if no duplicates.

    "First duplicate" means the earliest index where a value repeats.

    >>> find_first_duplicate([1, 2, 3, 2, 4])
    2
    >>> find_first_duplicate([1, 2, 3])
    """
    raise NotImplementedError


def sum_until_negative(nums: list[int]) -> int:
    """Sum integers from `nums` until (and excluding) the first negative number.

    >>> sum_until_negative([1, 2, 3, -1, 10])
    6
    >>> sum_until_negative([5, 5, 5])
    15
    """
    raise NotImplementedError
