#!/usr/bin/env python3
"""Inject reference solutions into exercise modules in-memory, then run pytest.

CI uses this to confirm the test suite matches the answer key. Learners
implement exercises/ themselves — this script is not part of the normal workflow.
"""

from __future__ import annotations

import importlib
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]

MODULE_ATTRS: dict[str, list[str]] = {
    "exercises.basics": [
        "reverse_string",
        "count_vowels",
        "fahrenheit_to_celsius",
        "truncate",
    ],
    "exercises.control_flow": [
        "is_palindrome",
        "fizzbuzz",
        "find_first_duplicate",
        "sum_until_negative",
    ],
    "exercises.functions": [
        "apply_twice",
        "make_multiplier",
        "merge_dicts",
        "greet",
    ],
    "exercises.data_structures": [
        "unique_sorted",
        "word_count",
        "flatten",
        "invert_dict",
    ],
    "exercises.oop": ["Rectangle", "BankAccount", "Animal", "Dog"],
    "exercises.exceptions": [
        "safe_divide",
        "parse_int",
        "validate_age",
        "read_first_line",
    ],
    "exercises.file_io": ["count_lines", "write_lines", "read_json_field"],
    "exercises.advanced": ["fibonacci", "batches", "timer", "suppress_exceptions"],
}


def inject_solutions() -> None:
    sys.path.insert(0, str(ROOT))
    sys.path.insert(0, str(ROOT / "grader"))

    import solutions as sol  # noqa: WPS433 — intentional grader import

    for module_name, attr_names in MODULE_ATTRS.items():
        module = importlib.import_module(module_name)
        for attr in attr_names:
            setattr(module, attr, getattr(sol, attr))


def main() -> int:
    inject_solutions()
    return pytest.main(["tests/", "-q"])


if __name__ == "__main__":
    raise SystemExit(main())
