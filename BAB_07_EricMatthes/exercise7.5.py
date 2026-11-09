prompt = "welcome to Solo teater, firstly can you tell me how old are you ?"
age = int(input(prompt))
if age < 3:
    print("Your ticket is free !")
elif age <= 12:
    print("Your ticket costs $10.")
else:
    print("Your ticket costs $15.")