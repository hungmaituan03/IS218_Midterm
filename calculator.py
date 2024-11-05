# calculator.py

import pandas as pd
from history import HistoryManager
from arithmetic import add, subtract, multiply, divide  # Import arithmetic functions

def main():
    print("Welcome to the Python Calculator!")
    print("Type 'menu' to see available commands.")
    
    history_manager = HistoryManager()

    while True:
        command = input("Enter command: ").strip().lower()

        if command in ['exit', 'quit']:
            print("Exiting calculator.")
            break
        elif command == 'menu':
            print("Available commands: add, subtract, multiply, divide, history, clear, load <filename>, save <filename>, exit")
            continue
        elif command == 'history':
            print(history_manager.show_history())
            continue
        elif command == 'clear':
            print(history_manager.clear_history())
            continue

        # Handle arithmetic commands
        try:
            parts = command.split()
            if len(parts) == 3:
                op, num1, num2 = parts[0], float(parts[1]), float(parts[2])
                
                if op == 'add':
                    result = add(num1, num2)
                elif op == 'subtract':
                    result = subtract(num1, num2)
                elif op == 'multiply':
                    result = multiply(num1, num2)
                elif op == 'divide':
                    result = divide(num1, num2)
                else:
                    print("Error: Unknown operation.")
                    continue

                print(f"Result: {result}")
                history_manager.add_to_history(command, result)
            elif len(parts) == 2 and parts[0] in ['load', 'save']:
                if parts[0] == 'load':
                    print(history_manager.load_history(parts[1]))
                elif parts[0] == 'save':
                    print(history_manager.save_history(parts[1]))
            else:
                print("Error: Invalid command format. Use: operation number1 number2")
        except ValueError:
            print("Error: Please ensure you are entering numbers.")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
