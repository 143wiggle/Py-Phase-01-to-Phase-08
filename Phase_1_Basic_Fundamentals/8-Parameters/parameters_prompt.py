# parameters_prompt.py
# Demonstrates positional and keyword parameters

def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Prompt user
user_name = input("Enter your name: ")
user_greeting = input("Enter a greeting (press Enter to use default): ")

if user_greeting.strip() == "":
    greet_user(user_name)
else:
    greet_user(user_name, user_greeting)
