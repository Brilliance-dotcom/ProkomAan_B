Prompt = ("Welcome to our restaurant, for how many people would you like to make a reservation ?")
answet = int(input(Prompt))
if answet > 8:
    print("I'm sorry, we don't have any available tables for that many people, please try again later !")
else:
    print("Your table is ready, please follow me to your table !")
    