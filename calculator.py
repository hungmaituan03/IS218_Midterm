"""
Advanced Python Calculator Module

This module implements a calculator that supports basic arithmetic operations,
history management, and a plugin system. It includes a command-line REPL interface.
"""

import ast
import logging
from history_manager import HistoryManager
from plugin_system import PluginSystem

class Calculator:
    """A class representing an advanced calculator with REPL and plugin capabilities."""
    def __init__(self):
        """Initializes the Calculator with logging, history management, and plugin system."""
        self.logger = self.setup_logging()
        self.history_manager = HistoryManager()
        self.plugin_system = PluginSystem()

    def setup_logging(self):
        """Sets up the logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )
        return logging.getLogger(__name__)

    def execute_operation(self, operation):
        """Executes an arithmetic operation and logs the result.

        Args:
            operation (str): The arithmetic expression to evaluate.

        Returns:
            The result of the operation or an error message if the operation is invalid.
        """
        try:
            # Safely parse the expression
            parsed_expr = ast.parse(operation, mode="eval")
            if not all(
                isinstance(
                    node,
                    (ast.Expression, ast.BinOp, ast.Constant, ast.UnaryOp, ast.operator),
                )
                for node in ast.walk(parsed_expr)
            ):
                raise ValueError("Invalid operation")

            # Use eval with caution; ensure inputs are from trusted sources
            result = eval(compile(parsed_expr, filename="", mode="eval"))
            self.history_manager.add_to_history(operation, result)
            self.logger.info("Executed operation: %s = %s", operation, result)
            return result
        except (SyntaxError, ValueError) as e:
            self.logger.error("Error executing operation: %s - %s", operation, e)
            return f"Error: {str(e)}"

    def start_repl(self):
        """Starts the calculator REPL loop."""
        print("Welcome to the Advanced Python Calculator")
        while True:
            user_input = input("Enter operation or 'exit' to quit: ").strip()
            if user_input.lower() == "exit":
                print("Exiting the calculator. Goodbye!")
                break
            if user_input.lower() == "history":
                print(self.history_manager.get_history())
            elif user_input.lower() == "clear history":
                self.history_manager.clear_history()
                print("History cleared.")
            elif user_input.lower() == "plugins":
                if hasattr(self.plugin_system, 'list_plugins'):
                    print("Available plugins:")
                    print(self.plugin_system.list_plugins())
            elif user_input.lower() == "menu":
                self.show_menu()
            else:
                result = self.execute_operation(user_input)
                print(result)

    def show_menu(self):
        """Displays the menu of commands for the calculator."""
        print("\nCalculator Menu:")
        print("1. Enter an arithmetic operation (e.g., 3 + 4)")
        print("2. Type 'history' to view calculation history")
        print("3. Type 'clear history' to clear the history")
        print("4. Type 'plugins' to list available plugins")
        print("5. Type 'menu' to display this menu")
        print("6. Type 'exit' to quit the application")
        print()

if __name__ == "__main__":
    calculator = Calculator()
    calculator.start_repl()
