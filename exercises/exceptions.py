"""Exercise 6: Exceptions and error handling."""


def safe_divide(a: float, b: float) -> float | None:
    """Return a / b, or None if b is zero.

    >>> safe_divide(10, 2)
    5.0
    >>> safe_divide(10, 0) is None
    True
    """
    raise NotImplementedError


def parse_int(s: str) -> int | None:
    """Parse `s` as an integer, returning None on failure.

    >>> parse_int("42")
    42
    >>> parse_int("not a number") is None
    True
    """
    raise NotImplementedError


def validate_age(age: int) -> int:
    """Return `age` if it is between 0 and 150 inclusive.

    Raise ValueError with a descriptive message otherwise.
    """
    raise NotImplementedError


def read_first_line(path: str) -> str | None:
    """Read and return the first line of a file (without trailing newline).

    Return None if the file does not exist.
    """
    raise NotImplementedError
