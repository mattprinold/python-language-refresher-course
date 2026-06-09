import pytest

from exercises import exceptions as ex


def test_safe_divide():
    assert ex.safe_divide(10, 2) == 5.0
    assert ex.safe_divide(10, 0) is None


def test_parse_int():
    assert ex.parse_int("42") == 42
    assert ex.parse_int("-7") == -7
    assert ex.parse_int("not a number") is None
    assert ex.parse_int("3.14") is None


def test_validate_age():
    assert ex.validate_age(0) == 0
    assert ex.validate_age(150) == 150
    with pytest.raises(ValueError, match="0.*150"):
        ex.validate_age(-1)
    with pytest.raises(ValueError, match="0.*150"):
        ex.validate_age(151)


def test_read_first_line(tmp_path):
    f = tmp_path / "sample.txt"
    f.write_text("first line\nsecond line\n")
    assert ex.read_first_line(str(f)) == "first line"
    assert ex.read_first_line(str(tmp_path / "missing.txt")) is None
