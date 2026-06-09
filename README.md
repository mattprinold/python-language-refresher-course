# Python Language Refresher Course

A hands-on Python refresher with **32 exercises** across 8 modules and an automated test suite. Clone it, fill in the stubs, and verify your work with `pytest`.

Designed for developers returning to Python after time away — or anyone who wants a quick, practical skills check.

## Requirements

- Python **3.10+** (uses modern type hints like `list[str]` and `int | None`)
- pip

## Quick start

```bash
git clone https://github.com/mattprinold/python-language-refresher-course.git
cd python-language-refresher-course

python3 -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

pytest tests/ -v                 # expect failures until you implement the exercises
```

## How to work through it

1. Open each file in `exercises/` in order (start with `basics.py`).
2. Read the docstrings — they describe what each function should do, with examples.
3. Replace `raise NotImplementedError` with your implementation.
4. Run tests as you go:

   ```bash
   pytest tests/test_01_basics.py -v   # one module
   pytest tests/ -v                    # full suite (55 tests)
   ```

5. When an exercise passes, move on. Partial completion is fine.

### Optional: AI-assisted review

If you use an AI coding assistant (e.g. Cursor), you can ask it to check your work after you're done:

> "Check my Python refresher answers"

It can read your implementations, run the test suite, and give feedback on failures and style.

## Exercise topics

| File | Topics | Exercises |
|------|--------|-----------|
| `basics.py` | Types, strings, slicing | 4 |
| `control_flow.py` | `if`/`elif`/`else`, `for`, `while` | 4 |
| `functions.py` | Defaults, closures, `*args` | 4 |
| `data_structures.py` | Lists, dicts, sets, comprehensions | 4 |
| `oop.py` | Classes, methods, inheritance | 4 |
| `exceptions.py` | `try`/`except`, raising errors | 4 |
| `file_io.py` | Files, `pathlib`, JSON | 3 |
| `advanced.py` | Generators, decorators, context managers | 4 |

## Tips

- Prefer idiomatic Python — comprehensions, `enumerate`, `with` statements — where they fit naturally.
- Read the test file if you're stuck; tests clarify edge cases without giving away the solution.
- **Spoiler:** reference solutions live in `grader/solutions.py`. Try every exercise yourself first.

## Project layout

```
language-refresher/
├── exercises/          # Your code goes here
├── tests/              # Automated tests (55 total)
├── grader/
│   ├── solutions.py    # Reference implementations (spoilers!)
│   └── check.py        # Convenience test runner
├── requirements.txt
└── pytest.ini
```

## Did you find this useful?

<a href="https://www.buymeacoffee.com/mattprinold" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me a Coffee" style="height: 60px !important;width: 217px !important;" ></a>

## License

MIT — see [LICENSE](LICENSE).
