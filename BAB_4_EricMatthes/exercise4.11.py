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