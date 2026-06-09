"""Exercise 7: File I/O and pathlib."""

import json
from pathlib import Path


def count_lines(path: str | Path) -> int:
    """Return the number of lines in the file at `path`.

    >>> import tempfile, os
    >>> with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt') as f:
    ...     f.write("line1\\nline2\\nline3\\n")
    ...     fname = f.name
    >>> count_lines(fname)
    3
    >>> os.unlink(fname)
    """
    raise NotImplementedError


def write_lines(path: str | Path, lines: list[str]) -> None:
    """Write each string in `lines` to `path`, one per line (with newlines)."""
    raise NotImplementedError


def read_json_field(path: str | Path, field: str):
    """Read a JSON file and return the value for `field`.

    Raise FileNotFoundError if the file doesn't exist.
    Raise KeyError if the field is missing.
    """
    raise NotImplementedError
