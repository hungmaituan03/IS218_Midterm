"""Test suite for testing the history functionality of the Calculator."""
from calculator import Calculator


def test_add_to_history():
    """Test that the history is correctly updated after an addition operation."""
    calculator_instance = Calculator()  # Initialize directly in the test
    calculator_instance.execute_operation("3 + 4")
    history = calculator_instance.history_manager.get_history()
    assert "3 + 4 = 7" in history


def test_clear_history():
    """Test that the history is cleared correctly."""
    calculator_instance = Calculator()  # Initialize directly in the test
    calculator_instance.execute_operation("10 - 5")
    calculator_instance.history_manager.clear_history()
    history = calculator_instance.history_manager.get_history()
    assert history == "History is empty"


def test_view_history():
    """Test that the history is correctly displayed after an operation."""
    calculator_instance = Calculator()  # Initialize directly in the test
    calculator_instance.execute_operation("2 * 3")
    history = calculator_instance.history_manager.get_history()
    assert "2 * 3 = 6" in history
