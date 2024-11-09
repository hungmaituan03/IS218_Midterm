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

    def safe_eval(self, expr):
        """Safely evaluates an arithmetic expression."""
        try:
            # Parse the expression into AST
            parsed_expr = ast.parse(expr, mode='eval')

            # Ensure only safe operations (numbers and arithmetic operations)
            if not all(
                isinstance(node, (ast.Expression, ast.BinOp, ast.Num, ast.UnaryOp, ast.operator))
                for node in ast.walk(parsed_expr)
            ):
                raise ValueError("Invalid operation")

            # Function to evaluate AST nodes
            def eval_node(node):
                if isinstance(node, ast.Num):  # A number
                    return node.n
                if isinstance(node, ast.BinOp):  # Binary operation
                    left = eval_node(node.left)
                    right = eval_node(node.right)
                    if isinstance(node.op, ast.Add):
                        return left + right
                    if isinstance(node.op, ast.Sub):
                        return left - right
                    if isinstance(node.op, ast.Mult):
                        return left * right
                    if isinstance(node.op, ast.Div):
                        return left / right
                    raise ValueError("Unsupported operator")
                if isinstance(node, ast.UnaryOp):  # Unary operation (e.g., negation)
                    operand = eval_node(node.operand)
                    if isinstance(node.op, ast.USub):
                        return -operand
                    raise ValueError("Unsupported unary operator")
                raise ValueError("Unsupported AST node")

            # Evaluate the expression
            return eval_node(parsed_expr.body)
        except (ValueError, TypeError) as e:
            self.logger.error("Error evaluating expression: %s", e)
            return f"Error: {str(e)}"

    def execute_operation(self, operation):
        """Executes an arithmetic operation and logs the result.

        Args:
            operation (str): The arithmetic expression to evaluate.

        Returns:
            The result of the operation or an error message if the operation is invalid.
        """
        try:
            # Safely evaluate the expression without using eval
            result = self.safe_eval(operation)
            if isinstance(result, (int, float)):
                self.history_manager.add_to_history(operation, result)
                self.logger.info("Executed operation: %s = %s", operation, result)
            return result
        except ValueError as e:
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
