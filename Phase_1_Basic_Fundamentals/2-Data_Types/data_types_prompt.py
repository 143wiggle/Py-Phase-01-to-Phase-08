# data_types_prompt.py
# Prompts the user for different types of data and prints the type of each using a function

def display_data_types(name, age, height, is_student):
    print("\n--- Data Types Summary ---")
    print("Name:", name, "| Type:", type(name))
    print("Age:", age, "| Type:", type(age))
    print("Height:", height, "| Type:", type(height))
    print("Is Student:", is_student, "| Type:", type(is_student))

# Prompting the user
name_input = input("Enter your name: ")
age_input = int(input("Enter your age: "))
height_input = float(input("Enter your height in meters (e.g., 1.75): "))
is_student_input = input("Are you a student? [yes/no]: ").strip().lower() == "yes"

# Call the function
display_data_types(name_input, age_input, height_input, is_student_input)
