# exceptions_prompt.py
# Demonstrates basic exception handling using try-except and a function

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Error: You can't divide by zero!")
    except ValueError:
        print("Error: Invalid value.")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Prompt user for input
try:
    num1 = float(input("Enter the numerator: "))
    num2 = float(input("Enter the denominator: "))
    divide_numbers(num1, num2)
except ValueError:
    print("Input must be a number.")
