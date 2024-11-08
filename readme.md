# Advanced Python Calculator

This repository contains the implementation of an Advanced Python Calculator with a command-line REPL interface. The calculator supports basic arithmetic operations, history management, and a plugin system.

## Features
- **Basic arithmetic operations**: Addition, subtraction, multiplication, and division.
- **History management**: Keeps track of previously executed operations.
- **Plugin system**: Extensible design for custom plugins.
- **Robust exception handling**: Implements both LBYL (Look Before You Leap) and EAFP (Easier to Ask for Forgiveness than Permission) principles.
- **Logging**: Integrated logging for audit and debugging purposes.

## Design Patterns Used
### Singleton Pattern
The `HistoryManager` is used as a singleton to ensure that only one instance manages the operation history. This approach ensures consistent state management throughout the application.

### Facade Pattern
The `Calculator` class acts as a facade that abstracts the complexities of interacting with `HistoryManager`, `PluginSystem`, and the logging setup, presenting a simplified interface for the REPL.

**Implementation Reference**:
- The singleton instance is created within the `Calculator` class:
```python
self.history_manager = HistoryManager()
```
- The plugin system is managed using:
```python
self.plugin_system = PluginSystem()
```
For more details, refer to the `Calculator` class in [calculator.py](./calculator.py).

## Environment Variables
**Description**:
Environment variables are used to set logging levels dynamically, allowing flexible configuration.

**Example**:
```python
import os
import logging

logging.basicConfig(
    level=os.getenv("CALCULATOR_LOG_LEVEL", "INFO"),
    format="%(asctime)s - %(levelname)s - %(message)s"
)
```
**Explanation**:
- The `os.getenv()` function reads the `CALCULATOR_LOG_LEVEL` variable, defaulting to `INFO` if it's not defined.
- This enables customizable logging behavior depending on the environment (development, testing, or production).

**Code Reference**:
See the `setup_logging` method in [calculator.py](./calculator.py).

## Logging
Logging is set up to provide structured logs for key operations and errors. This is helpful for tracking the flow of the program and diagnosing issues.

**Example**:
```python
def setup_logging(self):
    """Sets up the logging configuration."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger(__name__)

self.logger.info("Executed operation: %s = %s", operation, result)
self.logger.error("Error executing operation")
```
**Explanation**:
- Informational logs record successful operations.
- Error logs capture exceptions, making it easier to debug the program.

**Code Reference**:
Full logging setup and usage are implemented in [calculator.py](./calculator.py).

## Exception Handling: LBYL and EAFP
### LBYL (Look Before You Leap)
This approach is used to validate conditions before attempting operations.
```python
if not all(
    isinstance(
        node,
        (ast.Expression, ast.BinOp, ast.Constant, ast.UnaryOp, ast.operator),
    )
    for node in ast.walk(parsed_expr)
):
    raise ValueError("Invalid operation")
```
**Explanation**:
- Checks the parsed expression structure to ensure safety before evaluation.

### EAFP (Easier to Ask for Forgiveness than Permission)
This approach attempts execution directly and handles any resulting exceptions.
```python
try:
    result = eval(compile(parsed_expr, filename="", mode="eval"))
    self.history_manager.add_to_history(operation, result)
    self.logger.info("Executed operation: %s = %s", operation, result)
    return result
except (SyntaxError, ValueError) as e:
    self.logger.error("Error executing operation")
    return f"Error: {str(e)}"
```
**Explanation**:
- Safely attempts the operation and catches exceptions to handle errors gracefully.