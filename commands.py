# commands.py

from arithmetic import add, subtract, multiply, divide
from history import HistoryManager

def execute_command(command, history_manager):
    try:
        if command.startswith("add"):
            _, x, y = command.split()
            result = add(float(x), float(y))
            history_manager.add_entry(f"{x} + {y}", result)
            return result
        elif command.startswith("subtract"):
            _, x, y = command.split()
            result = subtract(float(x), float(y))
            history_manager.add_entry(f"{x} - {y}", result)
            return result
        elif command.startswith("multiply"):
            _, x, y = command.split()
            result = multiply(float(x), float(y))
            history_manager.add_entry(f"{x} * {y}", result)
            return result
        elif command.startswith("divide"):
            _, x, y = command.split()
            result = divide(float(x), float(y))
            history_manager.add_entry(f"{x} / {y}", result)
            return result
        elif command == "history":
            return history_manager.show_history()
        elif command.startswith("save history"):
            _, filename = command.split()
            history_manager.save_history(filename)
            return f"History saved to {filename}."
        elif command.startswith("load history"):
            _, filename = command.split()
            history_manager.load_history(filename)
            return f"History loaded from {filename}."
        elif command == "clear history":
            history_manager.clear_history()
            return "History cleared."
        elif command == "menu":
            return "Available commands: add, subtract, multiply, divide, history, save history [filename], load history [filename], clear history"
        else:
            return "Error: Unknown command."
    except Exception as e:
        return f"Error: {str(e)}"
