import pytest
from app.calculator import Calculator

def test_add():
    calc = Calculator()
    result = calc.execute_operation('3 + 2')
    assert result == 5

def test_subtract():
    calc = Calculator()
    result = calc.execute_operation('5 - 2')
    assert result == 3

def test_multiply():
    calc = Calculator()
    result = calc.execute_operation('2 * 3')
    assert result == 6

def test_divide():
    calc = Calculator()
    result = calc.execute_operation('6 / 3')
    assert result == 2
