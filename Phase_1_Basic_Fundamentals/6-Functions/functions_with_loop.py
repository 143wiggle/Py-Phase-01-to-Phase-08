# functions_with_loop.py
# Repeats the greeting function using a while loop

def greet_user(name, age):
    print(f"Hello {name}, you are {age} years old!")
    print("-" * 30)

while True:
    user_name = input("Enter your name: ")
    user_age = input("Enter your age: ")
    
    greet_user(user_name, user_age)

    again = input("Would you like to enter another? [Y/N]: ").strip().lower()
    if again != 'y':
        print("Goodbye!")
        break
