import pandas as pd
from collections import deque

class HistoryManager:
    def __init__(self):
        self.history = deque(maxlen=100)  # Limit history to 100 records
        self.df_history = pd.DataFrame(columns=["operation", "result"])

    def add_to_history(self, operation, result):
        try:
            self.history.append((operation, result))
            new_entry = pd.DataFrame([(operation, result)], columns=["operation", "result"])
            self.df_history = pd.concat([self.df_history, new_entry], ignore_index=True)
        except Exception as e:
            print(f"Error adding to history: {e}")

    def get_history(self):
        if not self.history:
            return "History is empty."
        return "\n".join([f"{record[0]} = {record[1]}" for record in self.history])

    def show_history(self):
        if not self.history:
            print("History is empty.")
        else:
            for record in self.history:
                print(f"{record[0]} = {record[1]}")

    def load_history_from_file(self, filename):
        try:
            df = pd.read_csv(filename)
            for _, row in df.iterrows():
                self.history.append((row['operation'], row['result']))
            self.df_history = pd.concat([self.df_history, df], ignore_index=True)
            print(f"Loaded history from {filename}")
        except Exception as e:
            print(f"Error loading history: {e}")

    def save_history_to_file(self, filename):
        try:
            self.df_history.to_csv(filename, index=False)
            print(f"Saved history to {filename}")
        except Exception as e:
            print(f"Error saving history: {e}")

    def clear_history(self):
        self.history.clear()
        self.df_history = pd.DataFrame(columns=["operation", "result"])
        print("Cleared history")
