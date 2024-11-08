import ast
import logging
from history_manager import HistoryManager
from plugin_system import PluginSystem

class Calculator:
    def __init__(self):
        self.logger = self.setup_logging()
        self.history_manager = HistoryManager()
        self.plugin_system = PluginSystem()

    def setup_logging(self):
        # Set up logging configuration
        logging.basicConfig(level=logging.INFO,
                            format="%(asctime)s - %(levelname)s - %(message)s")
        logger = logging.getLogger(__name__)
        return logger

    def execute_operation(self, operation):
        try:
            # Safely parse the expression
            parsed_expr = ast.parse(operation, mode='eval')
            if not all(isinstance(node, (ast.Expression, ast.BinOp, ast.Constant, ast.UnaryOp, ast.operator)) for node in ast.walk(parsed_expr)):
                raise ValueError("Invalid operation")

            result = eval(compile(parsed_expr, filename="", mode="eval"))
            # Pass the operation and result separately to add_to_history
            self.history_manager.add_to_history(operation, result)
            self.logger.info(f"Executed operation: {operation} = {result}")
            return result
        except (SyntaxError, ValueError) as e:
            self.logger.error(f"Error executing operation: {operation} - {e}")
            return f"Error: {str(e)}"

    def start_repl(self):
        print("Welcome to the Advanced Python Calculator")
        while True:
            user_input = input("Enter operation or 'exit' to quit: ").strip()
            if user_input.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                break
            elif user_input.lower() == 'history':
                print(self.history_manager.get_history())
            elif user_input.lower() == 'clear history':
                self.history_manager.clear_history()
                print("History cleared.")
            elif user_input.lower() == 'plugins':
                print("Available plugins:")
                print(self.plugin_system.list_plugins())
            elif user_input.lower() == 'menu':
                self.show_menu()
            else:
                result = self.execute_operation(user_input)
                print(result)

    def show_menu(self):
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
