from exercises import data_structures as ex


def test_unique_sorted():
    assert ex.unique_sorted([3, 1, 2, 1, 3]) == [1, 2, 3]
    assert ex.unique_sorted([]) == []


def test_word_count():
    assert ex.word_count("Hello hello world") == {"hello": 2, "world": 1}
    assert ex.word_count("") == {}


def test_flatten():
    assert ex.flatten([[1, 2], [3], [], [4, 5]]) == [1, 2, 3, 4, 5]
    assert ex.flatten([]) == []


def test_invert_dict():
    assert ex.invert_dict({"a": 1, "b": 2, "c": 1}) == {1: ["a", "c"], 2: ["b"]}
    assert ex.invert_dict({}) == {}
