import pytest

from exercises import basics as ex


@pytest.mark.parametrize(
    "s, expected",
    [
        ("hello", "olleh"),
        ("", ""),
        ("a", "a"),
        ("Python", "nohtyP"),
    ],
)
def test_reverse_string(s, expected):
    assert ex.reverse_string(s) == expected


@pytest.mark.parametrize(
    "s, expected",
    [
        ("Hello World", 3),
        ("xyz", 0),
        ("AEIOU", 5),
        ("", 0),
    ],
)
def test_count_vowels(s, expected):
    assert ex.count_vowels(s) == expected


@pytest.mark.parametrize(
    "f, expected",
    [
        (32, 0.0),
        (212, 100.0),
        (68, 20.0),
        (-40, -40.0),
    ],
)
def test_fahrenheit_to_celsius(f, expected):
    assert ex.fahrenheit_to_celsius(f) == expected


@pytest.mark.parametrize(
    "text, max_len, suffix, expected",
    [
        ("hello world", 8, "...", "hello..."),
        ("hi", 10, "...", "hi"),
        ("abcdef", 6, "...", "abcdef"),
        ("abcdef", 5, "..", "abc.."),
    ],
)
def test_truncate(text, max_len, suffix, expected):
    assert ex.truncate(text, max_len, suffix) == expected
