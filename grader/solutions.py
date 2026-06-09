"""Reference solutions — for the grader only. Don't peek until you've tried!"""

from contextlib import contextmanager
from functools import wraps
import json
import time
from pathlib import Path


# --- basics ---
def reverse_string(s: str) -> str:
    return s[::-1]


def count_vowels(s: str) -> int:
    return sum(1 for c in s.lower() if c in "aeiou")


def fahrenheit_to_celsius(f: float) -> float:
    return round((f - 32) * 5 / 9, 1)


def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    if len(text) <= max_len:
        return text
    return text[: max_len - len(suffix)] + suffix


# --- control_flow ---
def is_palindrome(s: str) -> bool:
    cleaned = "".join(c.lower() for c in s if c.isalnum())
    return cleaned == cleaned[::-1]


def fizzbuzz(n: int) -> list[str]:
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def find_first_duplicate(nums: list[int]) -> int | None:
    seen = set()
    for n in nums:
        if n in seen:
            return n
        seen.add(n)
    return None


def sum_until_negative(nums: list[int]) -> int:
    total = 0
    for n in nums:
        if n < 0:
            break
        total += n
    return total


# --- functions ---
def apply_twice(func, x):
    return func(func(x))


def make_multiplier(factor: int):
    def multiply(x):
        return x * factor

    return multiply


def merge_dicts(*dicts: dict) -> dict:
    result = {}
    for d in dicts:
        result.update(d)
    return result


def greet(name: str, greeting: str = "Hello", punctuation: str = "!") -> str:
    return f"{greeting}, {name}{punctuation}"


# --- data_structures ---
def unique_sorted(nums: list[int]) -> list[int]:
    return sorted(set(nums))


def word_count(text: str) -> dict[str, int]:
    counts: dict[str, int] = {}
    for word in text.split():
        key = word.lower()
        counts[key] = counts.get(key, 0) + 1
    return counts


def flatten(nested: list) -> list:
    return [item for sublist in nested for item in sublist]


def invert_dict(d: dict) -> dict:
    result: dict = {}
    for key, value in d.items():
        if value not in result:
            result[value] = [key]
        else:
            result[value].append(key)
    return result


# --- oop ---
class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    def area(self) -> float:
        return self.width * self.height

    def perimeter(self) -> float:
        return 2 * (self.width + self.height)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0) -> None:
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount


class Animal:
    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError


class Dog(Animal):
    def speak(self) -> str:
        return "Woof!"


# --- exceptions ---
def safe_divide(a: float, b: float) -> float | None:
    try:
        return a / b
    except ZeroDivisionError:
        return None


def parse_int(s: str) -> int | None:
    try:
        return int(s)
    except ValueError:
        return None


def validate_age(age: int) -> int:
    if not 0 <= age <= 150:
        raise ValueError(f"Age must be between 0 and 150, got {age}")
    return age


def read_first_line(path: str) -> str | None:
    try:
        with open(path) as f:
            return f.readline().rstrip("\n")
    except FileNotFoundError:
        return None


# --- file_io ---
def count_lines(path: str | Path) -> int:
    with open(path) as f:
        return sum(1 for _ in f)


def write_lines(path: str | Path, lines: list[str]) -> None:
    with open(path, "w") as f:
        for line in lines:
            f.write(line + "\n")


def read_json_field(path: str | Path, field: str):
    with open(path) as f:
        data = json.load(f)
    if field not in data:
        raise KeyError(field)
    return data[field]


# --- advanced ---
def fibonacci(n: int):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def batches(iterable, size: int):
    batch = []
    for item in iterable:
        batch.append(item)
        if len(batch) == size:
            yield batch
            batch = []
    if batch:
        yield batch


def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"{func.__name__} took {elapsed:.3f}s")
        return result

    return wrapper


@contextmanager
def suppress_exceptions(*exception_types):
    try:
        yield
    except exception_types:  # noqa: B904 — tuple of exception classes
        pass
