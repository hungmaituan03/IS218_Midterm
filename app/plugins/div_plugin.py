"""
Division Plugin

This plugin handles the division of two numbers and outputs the result.
"""

def execute():
    """Executes the division operation between two user-provided numbers.
    Prompts the user for two numbers, performs division, and handles errors
    such as division by zero and invalid inputs.
    """
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        if b == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = a / b
            print(f"{a} / {b} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
