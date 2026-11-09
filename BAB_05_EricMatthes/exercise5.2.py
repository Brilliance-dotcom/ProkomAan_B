#variabel
galaksi = 'milky way'
motorcycle = ['pcx', 'nmax', 'vario']
city = 'Solo'
nilai_prokom = 100

print("Is galaksi == 'milky way'? I predict True.")
print(galaksi == 'milky way')

print("\nIs galaksi == 'andromeda'? I predict False.")
print(galaksi == 'andromeda')

print("\nIs galaksi != 'andromeda'? I predict True.")
print(galaksi != 'andromeda')

print("\nIs galaksi != 'milky way'? I predict False.")
print(galaksi != 'milky way')

print("\n=======================================================================")

print("\nIs city.lower() == 'solo'? I predict True.")
print(city.lower() == 'solo')

print("\nIs city.lower() == 'SOLO'? I predict False.")
print(city.lower() == 'SOLO')

print("\n=======================================================================")

print("\nIs nilai_prokom == 100? I predict True.")
print(nilai_prokom == 100)
print("\nIs nilai_prokom == 90? I predict False.")
print(nilai_prokom == 90)

print("\nIs nilai_prokom != 90? I predict True.")
print(nilai_prokom != 90)
print("\nIs nilai_prokom != 100? I predict False.")
print(nilai_prokom != 100)

print("\nIs nilai_prokom > 90? I predict True.")
print(nilai_prokom > 90)
print("\nIs nilai_prokom > 100? I predict False.")
print(nilai_prokom > 100)

print("\nIs nilai_prokom < 110? I predict True.")
print(nilai_prokom < 110)
print("\nIs nilai_prokom < 100? I predict False.")
print(nilai_prokom < 100)

print("\nIs nilai_prokom >= 100? I predict True.")
print(nilai_prokom >= 100)
print("\nIs nilai_prokom >= 101? I predict False.")
print(nilai_prokom >= 101)

print("\nIs nilai_prokom <= 100? I predict True.")
print(nilai_prokom <= 100)
print("\nIs nilai_prokom <= 99? I predict False.")
print(nilai_prokom <= 99)

print("\n=======================================================================")

print("\nIs nilai_prokom >= 100 and nilai_prokom < 110? I predict True.")
print(nilai_prokom >= 100 and nilai_prokom < 110)
print("\nIs nilai_prokom >= 100 and nilai_prokom < 100? I predict False.")
print(nilai_prokom >= 100 and nilai_prokom < 100)

print("\nIs nilai_prokom < 100 or nilai_prokom == 110? I predict True.")
print(nilai_prokom < 100 or nilai_prokom == 110)
print("\nIs nilai_prokom < 100 or nilai_prokom > 110? I predict False.")
print(nilai_prokom < 100 or nilai_prokom > 110)

print("\n=======================================================================")

print("\nIs 'pcx' in motorcycle? I predict True.")
print('pcx' in motorcycle)
print("\nIs 'shogun' in motorcycle? I predict False.")
print('shogun' in motorcycle)

print("\n=======================================================================")

print("\nIs 'pcx' not in motorcycle? I predict False.")
print('pcx' not in motorcycle)
print("\nIs 'shogun' not in motorcycle? I predict True.")
print('shogun' not in motorcycle)