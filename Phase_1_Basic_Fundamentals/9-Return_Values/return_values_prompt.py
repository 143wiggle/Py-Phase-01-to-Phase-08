# return_values_prompt.py
# Function that returns a full name

def get_full_name(first, last):
    full_name = f"{first.strip().title()} {last.strip().title()}"
    return full_name

# Prompt user
first = input("Enter your first name: ")
last = input("Enter your last name: ")

result = get_full_name(first, last)
print(f"Full name: {result}")
