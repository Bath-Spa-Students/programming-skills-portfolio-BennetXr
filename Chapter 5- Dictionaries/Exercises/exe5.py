# Make an empty list to store the pets in.
pets = []

# Make individual pets, and store each one in the list.
pet = { 'animal': 'monkey', 'name': 'sai', 'owner': 'josef','weight': 86,'eats': 'banana',}
pets.append(pet)

pet = {'animal': 'snake','name': 'ramo','owner': 'jyothir','weight': 10,'eats': 'milk',}
pets.append(pet)

pet = {'animal': 'hippopotamus','name': 'unni','owner': 'bennett','weight': 300,'eats': 'chocolate',}
pets.append(pet)

# Display information about each pet.
for pet in pets:
    print("\nHere's what I know about " + pet['name'].title() + ":")
    for key, value in pet.items():
        print("\t" + key + ": " + str(value))
