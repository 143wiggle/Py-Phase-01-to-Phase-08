# return_values_with_loop.py
# Uses return values to format multiple full names

def get_full_name(first, last):
    full_name = f"{first.strip().title()} {last.strip().title()}"
    return full_name

while True:
    first = input("Enter your first name: ")
    last = input("Enter your last name: ")

    result = get_full_name(first, last)
    print(f"Full name: {result}")

    again = input("Do you want to enter another name? [Y/N]: ").strip().lower()
    if again != 'y':
        print("Done collecting names.")
        break
