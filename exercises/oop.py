"""Exercise 5: Object-oriented programming."""


class Rectangle:
    """A rectangle defined by width and height."""

    def __init__(self, width: float, height: float) -> None:
        raise NotImplementedError

    def area(self) -> float:
        """Return the area."""
        raise NotImplementedError

    def perimeter(self) -> float:
        """Return the perimeter."""
        raise NotImplementedError

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


class BankAccount:
    """A simple bank account with deposit and withdraw."""

    def __init__(self, owner: str, balance: float = 0.0) -> None:
        raise NotImplementedError

    def deposit(self, amount: float) -> None:
        """Add `amount` to the balance. Amount must be positive."""
        raise NotImplementedError

    def withdraw(self, amount: float) -> None:
        """Subtract `amount` from the balance.

        Raises ValueError if amount is negative or exceeds balance.
        """
        raise NotImplementedError


class Animal:
    """Base class for animals."""

    def __init__(self, name: str) -> None:
        self.name = name

    def speak(self) -> str:
        raise NotImplementedError


class Dog(Animal):
    """A dog that says Woof."""

    def speak(self) -> str:
        raise NotImplementedError
