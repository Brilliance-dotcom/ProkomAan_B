pet_1 = {'animal': 'ferret', 'owner': 'Andi'}
pet_2 = {'animal': 'pig', 'owner': 'Budi'}
pet_3 = {'animal': 'rabbit', 'owner': 'Citra'}
pet_4 = {'animal': 'parrot', 'owner': 'Dewi'}

pets = [pet_1, pet_2, pet_3, pet_4]

for pet in pets:
    print("\nPet information:")
    for key, value in pet.items():
        print(f"  {key.title()}: {value}")