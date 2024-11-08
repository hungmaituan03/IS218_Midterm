from collections import deque
import pandas as pd


class HistoryManager:
    """A class to manage the history of operations in the calculator."""

    def __init__(self):
        """Initializes the history manager with a deque for storing operations."""
        self.history = deque()

    def add_to_history(self, operation, result):
        """Adds an operation and its result to the history.

        Args:
            operation (str): The operation performed.
            result: The result of the operation.
        """
        try:
            entry = {"operation": operation, "result": result}
            self.history.append(entry)
        except (TypeError, ValueError) as e:
            print(f"Failed to add entry to history: {e}")

    def get_history(self):
        """Returns the history of operations as a formatted string.

        Returns:
            str: A string representation of the operation history.
        """
        if not self.history:
            return "History is empty"

        history_str = []
        for entry in self.history:
            history_str.append(f"{entry['operation']} = {entry['result']}")

        return "\n".join(history_str)

    def clear_history(self):
        """Clears the history of operations."""
        try:
            self.history.clear()
        except RuntimeError as e:
            print(f"Failed to clear history: {e}")

    def save_history_to_csv(self, filename):
        """Saves the history to a CSV file.

        Args:
            filename (str): The name of the file to save the history.
        """
        try:
            df = pd.DataFrame(list(self.history))
            df.to_csv(filename, index=False)
        except (OSError, pd.errors.EmptyDataError) as e:
            print(f"Failed to save history to CSV: {e}")

    def load_history_from_csv(self, filename):
        """Loads history from a CSV file.

        Args:
            filename (str): The name of the file to load the history from.
        """
        try:
            df = pd.read_csv(filename)
            self.history = deque(df.to_dict("records"))
        except (OSError, pd.errors.EmptyDataError, pd.errors.ParserError) as e:
            print(f"Failed to load history from CSV: {e}")
