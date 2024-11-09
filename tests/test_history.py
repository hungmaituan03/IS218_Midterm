import pytest
from calculator import Calculator

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance for testing."""
    return Calculator()

def test_add_to_history(calculator):
    calculator.execute_operation("3 + 4")
    history = calculator.history_manager.get_history()
    assert "3 + 4 = 7" in history

def test_clear_history(calculator):
    calculator.execute_operation("10 - 5")
    calculator.history_manager.clear_history()
    history = calculator.history_manager.get_history()
    assert history == "History is empty"

def test_view_history(calculator):
    calculator.execute_operation("2 * 3")
    history = calculator.history_manager.get_history()
    assert "2 * 3 = 6" in history
