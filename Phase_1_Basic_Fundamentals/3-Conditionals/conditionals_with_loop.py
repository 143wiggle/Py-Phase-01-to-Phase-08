# conditionals_with_loop.py
# Repeats age group classification using a while loop

def check_age_group(age):
    if age < 13:
        print("You are a child.")
    elif 13 <= age <= 19:
        print("You are a teenager.")
    elif 20 <= age <= 59:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

while True:
    age_input = int(input("Enter your age: "))
    check_age_group(age_input)

    again = input("Would you like to try another age? [Y/N]: ").strip().lower()
    if again != 'y':
        print("Goodbye!")
        break
