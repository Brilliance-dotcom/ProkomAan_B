from pathlib import Path
import json

name = input("What is your name? ")
age = input("How old are you? ")
city = input("Which city do you live in? ")

user_info = {
    "name": name,
    "age": age,
    "city": city,
}

path = Path("user_info.json")
contents = json.dumps(user_info)
path.write_text(contents)

# Baca kembali data dari file
contents = path.read_text()
remembered = json.loads(contents)

print("\nHere is what I remember about you:")
print(f"Name: {remembered['name']}")
print(f"Age: {remembered['age']}")
print(f"City: {remembered['city']}")