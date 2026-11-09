Username = []

for name in Username:
    if name == 'admin':
        print(f"Good seeing you {name}, would you like to see today's report ?")
    else:
        print(f"Hello {name}, thank you for logging in what can i help you with today ?")
if Username == []:
    print("we need to find new user !!")