# function_definitions_prompt.py
# Function to calculate the price after an optional discount

def calculate_discounted_price(price, discount_rate=0.0):
    discounted = price - (price * discount_rate)
    return round(discounted, 2)

# Prompt user
try:
    price = float(input("Enter the original price: "))
    discount_input = input("Enter discount rate (e.g., 0.20 for 20% off, press Enter for no discount): ")

    if discount_input.strip() == "":
        final_price = calculate_discounted_price(price)
    else:
        discount = float(discount_input)
        final_price = calculate_discounted_price(price, discount)

    print(f"Final price after discount: {final_price}")
except ValueError:
    print("Please enter valid numbers.")
