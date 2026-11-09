prompt = "if you could just leave everything right now, and go to any place in the world, where would you go ?"
responses = {}

while True:
    name = input("\nWhat is your name? ")
    response = input(prompt)

    responses[name] = response

    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        break

print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name}: {response}")