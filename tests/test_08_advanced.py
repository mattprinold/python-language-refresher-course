import time

import pytest

from exercises import advanced as ex


def test_fibonacci():
    assert list(ex.fibonacci(0)) == []
    assert list(ex.fibonacci(1)) == [0]
    assert list(ex.fibonacci(7)) == [0, 1, 1, 2, 3, 5, 8]


def test_batches():
    assert list(ex.batches([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    assert list(ex.batches([], 3)) == []
    assert list(ex.batches([1], 5)) == [[1]]


def test_timer(capsys):
    @ex.timer
    def slow():
        time.sleep(0.05)

    slow()
    captured = capsys.readouterr()
    assert "slow took" in captured.out
    assert "s" in captured.out


def test_suppress_exceptions():
    with ex.suppress_exceptions(ValueError):
        raise ValueError("ignored")

    with pytest.raises(TypeError):
        with ex.suppress_exceptions(ValueError):
            raise TypeError("not ignored")
