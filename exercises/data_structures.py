"""Exercise 4: Data structures — lists, dicts, sets, and comprehensions."""


def unique_sorted(nums: list[int]) -> list[int]:
    """Return unique values from `nums` in ascending order.

    >>> unique_sorted([3, 1, 2, 1, 3])
    [1, 2, 3]
    """
    raise NotImplementedError


def word_count(text: str) -> dict[str, int]:
    """Return a dict mapping each word (lowercased) to its count.

    Words are separated by whitespace. Punctuation attached to words counts
    as part of the word (e.g. "hello," is one word).

    >>> word_count("Hello hello world")
    {'hello': 2, 'world': 1}
    """
    raise NotImplementedError


def flatten(nested: list) -> list:
    """Flatten a list one level deep.

    >>> flatten([[1, 2], [3], [], [4, 5]])
    [1, 2, 3, 4, 5]
    """
    raise NotImplementedError


def invert_dict(d: dict) -> dict:
    """Swap keys and values. If multiple keys share a value, collect keys in a list.

    >>> invert_dict({"a": 1, "b": 2, "c": 1})
    {1: ['a', 'c'], 2: ['b']}
    """
    raise NotImplementedError
