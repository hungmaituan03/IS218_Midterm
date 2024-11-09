"""Test suite for testing the history functionality of the Calculator."""

from calculator import Calculator

def test_add_to_history():
    """Test that the history is correctly updated after an addition operation."""
    # Initialize the Calculator instance directly in the test
    calculator = Calculator()
    calculator.execute_operation("3 + 4")
    history = calculator.history_manager.get_history()
    assert "3 + 4 = 7" in history


def test_clear_history():
    """Test that the history is cleared correctly."""
    # Initialize the Calculator instance directly in the test
    calculator = Calculator()
    calculator.execute_operation("10 - 5")
    calculator.history_manager.clear_history()
    history = calculator.history_manager.get_history()
    assert history == "History is empty"


def test_view_history():
    """Test that the history is correctly displayed after an operation."""
    # Initialize the Calculator instance directly in the test
    calculator = Calculator()
    calculator.execute_operation("2 * 3")
    history = calculator.history_manager.get_history()
    assert "2 * 3 = 6" in history
