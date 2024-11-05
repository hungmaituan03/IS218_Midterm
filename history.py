# history.py

import pandas as pd


class HistoryManager:
    def __init__(self):
        self.history = pd.DataFrame(columns=["Expression", "Result"])

    def add_to_history(self, expression, result):
        new_entry = pd.DataFrame(
            [[expression, result]], columns=["Expression", "Result"]
        )
        self.history = pd.concat([self.history, new_entry], ignore_index=True)

    def show_history(self):
        if self.history.empty:
            return "History is empty."
        return self.history

    def clear_history(self):
        self.history = pd.DataFrame(columns=["Expression", "Result"])
        return "History cleared."

    def save_history(self, filename):
        self.history.to_csv(filename, index=False)
        return f"History saved to {filename}."

    def load_history(self, filename):
        try:
            self.history = pd.read_csv(filename)
            return f"History loaded from {filename}."
        except Exception as e:
            return f"Error loading history: {e}"
