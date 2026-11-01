favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'rust',
'phil': 'python',
}
Responden = ['jen', 'Otid', 'phil', 'ucup', 'xavier']
for Responden in Responden:
    if Responden in favorite_languages:
        print (f"{Responden}, thank you for responding")
    else:
        print (f"{Responden}, since you haven't fill out the poll I invite you to fill out the poll!")


