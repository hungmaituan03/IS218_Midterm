# plugins/div_plugin.py

def execute():
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
