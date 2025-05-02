# list_with_loop.py
# Demonstrates using loops to interact with lists

# Create a list of fruits
fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Print each fruit using a loop
print("List of fruits:")
for fruit in fruits:
    print(fruit)

# Modify list by appending a new fruit
fruits.append("fig")
print("\nAdded 'fig':", fruits)

# Loop with index
print("\nUsing index to access items:")
for i in range(len(fruits)):
    print(f"{i + 1}: {fruits[i]}")

# Loop with condition
print("\nFruits that start with 'b':")
for fruit in fruits:
    if fruit.lower().startswith("b"):
        print(fruit)
