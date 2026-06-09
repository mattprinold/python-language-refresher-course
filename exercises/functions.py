"""Exercise 3: Functions — parameters, closures, and higher-order functions."""


def apply_twice(func, x):
    """Apply `func` to `x` twice: func(func(x)).

    >>> apply_twice(lambda n: n + 1, 3)
    5
    """
    raise NotImplementedError


def make_multiplier(factor: int):
    """Return a function that multiplies its argument by `factor`.

    >>> double = make_multiplier(2)
    >>> double(5)
    10
    """
    raise NotImplementedError


def merge_dicts(*dicts: dict) -> dict:
    """Merge multiple dicts left-to-right; later dicts override earlier keys.

    >>> merge_dicts({"a": 1}, {"b": 2}, {"a": 3})
    {'a': 3, 'b': 2}
    """
    raise NotImplementedError


def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:
    """Return a greeting string using the given defaults.

    >>> greet("Alice")
    'Hello, Alice!'
    >>> greet("Bob", greeting="Hi", punctuation=".")
    'Hi, Bob.'
    """
    raise NotImplementedError
