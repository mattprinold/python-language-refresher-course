import json

import pytest

from exercises import file_io as ex


def test_count_lines(tmp_path):
    f = tmp_path / "lines.txt"
    f.write_text("a\nb\nc\n")
    assert ex.count_lines(f) == 3
    assert ex.count_lines(str(f)) == 3


def test_write_lines(tmp_path):
    f = tmp_path / "out.txt"
    ex.write_lines(f, ["one", "two", "three"])
    assert f.read_text() == "one\ntwo\nthree\n"


def test_read_json_field(tmp_path):
    f = tmp_path / "data.json"
    f.write_text(json.dumps({"name": "Alice", "age": 30}))
    assert ex.read_json_field(f, "name") == "Alice"
    with pytest.raises(KeyError):
        ex.read_json_field(f, "missing")
    with pytest.raises(FileNotFoundError):
        ex.read_json_field(tmp_path / "nope.json", "name")
