# parameters_with_loop.py
# Demonstrates repeated use of parameters in a loop

def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

while True:
    user_name = input("Enter your name: ")
    user_greeting = input("Enter a greeting (press Enter to use default): ")

    if user_greeting.strip() == "":
        greet_user(user_name)
    else:
        greet_user(user_name, user_greeting)

    again = input("Greet another person? [Y/N]: ").strip().lower()
    if again != 'y':
        print("Session ended.")
        break
