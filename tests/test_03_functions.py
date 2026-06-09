from exercises import functions as ex


def test_apply_twice():
    assert ex.apply_twice(lambda n: n + 1, 3) == 5
    assert ex.apply_twice(lambda n: n * 2, 4) == 16


def test_make_multiplier():
    double = ex.make_multiplier(2)
    triple = ex.make_multiplier(3)
    assert double(5) == 10
    assert triple(4) == 12


def test_merge_dicts():
    assert ex.merge_dicts({"a": 1}, {"b": 2}, {"a": 3}) == {"a": 3, "b": 2}
    assert ex.merge_dicts() == {}
    assert ex.merge_dicts({"x": 1}) == {"x": 1}


def test_greet():
    assert ex.greet("Alice") == "Hello, Alice!"
    assert ex.greet("Bob", greeting="Hi", punctuation=".") == "Hi, Bob."
