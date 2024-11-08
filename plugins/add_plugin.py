# plugins/add_plugin.py

def execute():
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
        result = a + b
        print(f"{a} + {b} = {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
