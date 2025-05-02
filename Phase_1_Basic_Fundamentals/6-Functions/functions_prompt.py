# functions_prompt.py
# Simple user-defined function example

def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old!")

# Prompt user
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")

# Call function
greet_user(user_name, user_age)
