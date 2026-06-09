"""Exercise 1: Basics — types, strings, and simple operations."""


def reverse_string(s: str) -> str:
    """Return the reverse of `s`.

    >>> reverse_string("hello")
    'olleh'
    """
    raise NotImplementedError


def count_vowels(s: str) -> int:
    """Return the number of vowels (a, e, i, o, u) in `s`, case-insensitive.

    >>> count_vowels("Hello World")
    3
    """
    raise NotImplementedError


def fahrenheit_to_celsius(f: float) -> float:
    """Convert Fahrenheit to Celsius, rounded to 1 decimal place.

    >>> fahrenheit_to_celsius(32)
    0.0
    >>> fahrenheit_to_celsius(212)
    100.0
    """
    raise NotImplementedError


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Truncate `text` to at most `max_len` characters, appending `suffix` if truncated.

    The returned string must be at most `max_len` characters total.
    If no truncation is needed, return `text` unchanged (no suffix).

    >>> truncate("hello world", 8)
    'hello...'
    >>> truncate("hi", 10)
    'hi'
    """
    raise NotImplementedError
