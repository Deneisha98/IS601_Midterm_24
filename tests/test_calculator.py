import pytest
from calculator.main import Calculator

@pytest.fixture
def calculator():
    return Calculator()

def test_add(calculator: Any):
    assert calculator.add(3, 2) == 5

def test_subtract(calculator: Any):
    assert calculator.subtract(3, 2) == 1

def test_multiply(calculator: Any):
    assert calculator.multiply(3, 2) == 6

def test_divide(calculator: Any):
    assert calculator.divide(6, 2) == 3

def test_divide_by_zero(calculator: Any):
    with pytest.raises(ValueError):
        calculator.divide(6, 0)
