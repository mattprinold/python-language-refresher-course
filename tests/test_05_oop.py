import pytest

from exercises.oop import Animal, BankAccount, Dog, Rectangle


def test_rectangle():
    r = Rectangle(3, 4)
    assert r.width == 3
    assert r.height == 4
    assert r.area() == 12
    assert r.perimeter() == 14
    assert "Rectangle(width=3" in repr(r)


def test_bank_account_deposit():
    acct = BankAccount("Alice", 100)
    acct.deposit(50)
    assert acct.balance == 150
    assert acct.owner == "Alice"


def test_bank_account_withdraw():
    acct = BankAccount("Bob", 100)
    acct.withdraw(30)
    assert acct.balance == 70


def test_bank_account_withdraw_insufficient():
    acct = BankAccount("Bob", 50)
    with pytest.raises(ValueError):
        acct.withdraw(100)


def test_bank_account_deposit_negative():
    acct = BankAccount("Bob", 50)
    with pytest.raises(ValueError):
        acct.deposit(-10)


def test_dog_inheritance():
    dog = Dog("Rex")
    assert dog.name == "Rex"
    assert dog.speak() == "Woof!"
    assert isinstance(dog, Animal)
