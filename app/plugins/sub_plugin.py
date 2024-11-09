"""
Subtraction Plugin

This plugin handles the subtraction of two numbers and outputs the result.
"""

def execute():
    """Executes the subtraction operation between two user-provided numbers.
    Prompts the user for two numbers, performs subtraction, and handles
    invalid input errors.
    """
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = a - b
        print(f"{a} - {b} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
