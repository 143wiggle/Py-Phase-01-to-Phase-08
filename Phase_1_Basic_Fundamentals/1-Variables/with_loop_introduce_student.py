# with_loop_introduce_student.py
# A simple program that repeatedly introduces students using user input and a while loop

def introduce_student(name, age, course, year_level):
    print("\n--- Student Introduction ---")
    print(f"My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I am studying {course}.")
    print(f"I am in year level {year_level}.")
    print("Nice to meet you!\n")

# Start of the loop
while True:
    # Prompting the user for student details
    student_name = input("Enter your name: ")
    student_age = int(input("Enter your age: "))
    student_course = input("Enter your course: ")
    student_year = input("Enter your year level (e.g., 1st Year, 2nd Year): ")

    # Calling the function
    introduce_student(student_name, student_age, student_course, student_year)

    # Ask if the user wants to do another
    repeat = input("Would you like another introduction? [Y/N]: ").strip().lower()
    if repeat != 'y':
        print("Program ended.")
        break
