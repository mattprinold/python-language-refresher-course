#!/usr/bin/env python3
"""Run the test suite and print a summary for grading."""

import subprocess
import sys


def main() -> int:
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/", "-v", "--tb=no", "-q"],
        cwd=str(__import__("pathlib").Path(__file__).resolve().parent.parent),
    )
    return result.returncode


if __name__ == "__main__":
    raise SystemExit(main())
