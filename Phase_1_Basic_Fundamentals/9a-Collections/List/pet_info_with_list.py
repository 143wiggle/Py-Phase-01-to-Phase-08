# Function to collect pet information and display a summary using lists
def get_pet_info_with_list():
    # Prompt for number of pets
    num_pets = int(input("How many pets do you have? "))
    
    # Initialize an empty list to store pet details
    pets_info = []
    
    # Loop to collect information for each pet
    for i in range(num_pets):
        print(f"\nEnter details for Pet {i + 1}:")
        pet_name = input("What is your pet's name? ")
        pet_fruit = input(f"What is {pet_name}'s favorite fruit? ")
        
        # Store each pet's info as a dictionary in the list
        pet = {"name": pet_name, "favorite_fruit": pet_fruit}
        pets_info.append(pet)
    
    # Displaying the summary
    print("\n--- Pet Summary ---")
    for i, pet in enumerate(pets_info, start=1):
        pet_name = pet["name"]
        pet_fruit = pet["favorite_fruit"]
        print(f"Pet {i}: {pet_name} - Favorite Fruit: {pet_fruit}")

# Call the function
get_pet_info_with_list()
