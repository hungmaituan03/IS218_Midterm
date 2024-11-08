"""
Unit tests for the Calculator class.
"""

import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance for testing."""
    return Calculator()

def test_addition(calculator):
    """Test the addition operation."""
    result = calculator.execute_operation("3 + 4")
    assert result == 7

def test_subtraction(calculator):
    """Test the subtraction operation."""
    result = calculator.execute_operation("10 - 5")
    assert result == 5

def test_multiplication(calculator):
    """Test the multiplication operation."""
    result = calculator.execute_operation("2 * 3")
    assert result == 6

def test_division(calculator):
    """Test the division operation."""
    result = calculator.execute_operation("9 / 3")
    assert result == 3
