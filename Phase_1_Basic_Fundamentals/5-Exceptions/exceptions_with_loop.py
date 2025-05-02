# exceptions_with_loop.py
# Adds a loop for repeated exception handling tests

def divide_numbers(a, b):
    try:
        result = a / b
        print(f"The result of {a} divided by {b} is {result}")
    except ZeroDivisionError:
        print("Error: You can't divide by zero!")
    except Exception as e:
        print(f"Unexpected error: {e}")
    print("-" * 30)

while True:
    try:
        num1 = float(input("Enter the numerator: "))
        num2 = float(input("Enter the denominator: "))
        divide_numbers(num1, num2)
    except ValueError:
        print("Error: Please enter a valid number.")

    again = input("Would you like to try again? [Y/N]: ").strip().lower()
    if again != 'y':
        print("Done handling exceptions!")
        break
