"""Exercise 8: Generators, decorators, and context managers."""

import time
from contextlib import contextmanager
from functools import wraps


def fibonacci(n: int):
    """Yield the first `n` Fibonacci numbers starting with 0, 1, 1, 2, ...

    >>> list(fibonacci(7))
    [0, 1, 1, 2, 3, 5, 8]
    """
    raise NotImplementedError


def batches(iterable, size: int):
    """Yield successive chunks of `iterable` with at most `size` items.

    >>> list(batches([1, 2, 3, 4, 5], 2))
    [[1, 2], [3, 4], [5]]
    """
    raise NotImplementedError


def timer(func):
    """Decorator that prints execution time in seconds (3 decimal places).

    Print format: "<function_name> took X.XXXs"
      e.g. "slow took 0.102s"
    """
    raise NotImplementedError


@contextmanager
def suppress_exceptions(*exception_types):
    """Context manager that suppresses the given exception types.

    >>> with suppress_exceptions(ValueError):
    ...     raise ValueError("ignored")
    >>> with suppress_exceptions(ValueError):
    ...     raise TypeError("not ignored")  # doctest: +IGNORE_EXCEPTION_DETAIL
    Traceback (most recent call last):
    TypeError: not ignored
    """
    raise NotImplementedError
