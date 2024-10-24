import pytest
from calculator.main import Calculator # type: ignore

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator: any):
    assert calculator.add(3, 2) == 5

def test_subtract(calculator: any):
    assert calculator.subtract(3, 2) == 1

def test_multiply(calculator: any):
    assert calculator.multiply(3, 2) == 6

def test_divide(calculator: any):
    assert calculator.divide(6, 2) == 3

def test_divide_by_zero(calculator: any):
    with pytest.raises(ValueError):
        calculator.divide(6, 0)
