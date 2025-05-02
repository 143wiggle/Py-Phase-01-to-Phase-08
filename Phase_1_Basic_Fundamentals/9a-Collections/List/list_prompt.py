# list_prompt.py
# Demonstrates the creation, modification, and usage of lists

# Create an empty list and prompt for items
fruits = []

# Ask user for fruit names and add them to the list
while True:
    fruit = input("Enter a fruit name (or type 'done' to finish): ").strip()
    if fruit.lower() == "done":
        break
    fruits.append(fruit)

# Show the list after items have been added
print("\nYour list of fruits:")
print(fruits)

# Modify list: Add an item
fruits.append("mango")
print("\nAdded 'mango':", fruits)

# Remove an item
removed_fruit = fruits.pop(0)  # Remove first item
print("\nRemoved the first item:", removed_fruit, fruits)

# Access list by index
second_fruit = fruits[1] if len(fruits) > 1 else "No second fruit"
print("\nSecond fruit:", second_fruit)
