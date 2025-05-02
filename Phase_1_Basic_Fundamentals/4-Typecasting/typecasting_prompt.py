# typecasting_prompt.py
# A program that converts data types using typecasting and a function

def typecast_values(integer_value, float_value, boolean_value):
    # Converting integer to string
    print(f"Integer to String: {str(integer_value)} | Type: {type(str(integer_value))}")

    # Converting float to integer (losing decimal part)
    print(f"Float to Integer: {int(float_value)} | Type: {type(int(float_value))}")

    # Converting boolean to integer (True = 1, False = 0)
    print(f"Boolean to Integer: {int(boolean_value)} | Type: {type(int(boolean_value))}")

# Prompting user for values
int_input = int(input("Enter an integer value: "))
float_input = float(input("Enter a floating-point value: "))
bool_input = input("Enter a boolean value (True/False): ").strip().lower() == "true"

# Calling the function to demonstrate typecasting
typecast_values(int_input, float_input, bool_input)
