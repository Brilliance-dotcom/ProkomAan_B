Username = ['Funixxxxx', 'Davidtinez_', 'Lumo', 'Kaaazzz', 'A4n25',]
New_username = ['Davidtinez_', 'Lumo', "Waterymelon59", 'Beaconcream', 'Squarepants']

current_username = [user.lower() for user in Username]

for New_username in New_username:
    if New_username.lower() in current_username:
        print(f"the {New_username} already taken, please change into a new username")
    else:
        print(f"The {New_username} available")