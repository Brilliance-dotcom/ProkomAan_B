Person_0 = {'first_name' : 'william', 'last_name' : 'afton', 'age' : '40', 'city' : 'Los Angels'}
Person_1 = {'first_name' : 'Jeffrey', 'last_name' : 'Dahmer', 'age' : '32', 'city' : 'Milwaukee'}
Person_2 = {'first_name' : 'Hanib', 'Nurhaimin' : 'afton', 'age' : '50', 'city' : 'Bangkok'}
Person = [Person_0, Person_1, Person_2]
for Person in Person:
    print("============================")
    for key, value in Person.items():
        print(f"{key} : {value}")
print("============================")