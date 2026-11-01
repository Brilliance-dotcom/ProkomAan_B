sandwich_orders =  ['pastrami', 'pastrami', 'pastrami', 'pastrami', 'chicken', 'pastrami', 'beef']
finished_sandwiches = []
print("I'm sorry, we have run out of pastrami today !")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    if current_sandwich == 'pastrami':
        continue
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")