# conditionals_prompt.py
# A program that checks age group using if-elif-else and a function

def check_age_group(age):
    if age < 13:
        print("You are a child.")
    elif 13 <= age <= 19:
        print("You are a teenager.")
    elif 20 <= age <= 59:
        print("You are an adult.")
    else:
        print("You are a senior citizen.")

# Prompt user
age_input = int(input("Enter your age: "))
check_age_group(age_input)
