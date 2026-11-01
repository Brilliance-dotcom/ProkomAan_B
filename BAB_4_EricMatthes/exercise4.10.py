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
