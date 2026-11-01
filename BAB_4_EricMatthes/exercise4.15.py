#4.2
Pets = ["Racoon", "Fox", "Ferret"]
for pet in Pets:
    print(pet)
    if pet == "Racoon":
        print("they are so cute when they wash their food before eating it")
    if pet == "Fox":
        print("They have a very unique sound it's like a human laughing!")
    if pet == "Ferret":
            print("Their bones is so flexible")
print("\nThese animals are rare to be a pet, you gotta give it a try!")
#4.10
print("=======================================================================")
cubes = [number **3 for number in range(1, 11)]
print(cubes)
print("The first three cubed numbers in the list are :")
for number in cubes[:3]:
    print(number)
print("The middle three cubed numbers in the list are :")
for number in cubes[4:7]:
    print(number)
print("The last three cubed numbers in the list are :")
for number in cubes[-3:]:
    print(number)
#4.11
print("=======================================================================")
Pizzas = ["Meat Lovers", "Stuffed Crust", "Deep Dish"]
Friend_Pizzas = Pizzas[:]
Pizzas.append("Hawaiian")
Friend_Pizzas.append("margherita")
print("My favorite pizzas are :")
for pizza in Pizzas:
    print(pizza)
print("\nMy friend's favorite pizzas are :")
for pizza in Friend_Pizzas:
    print(pizza)