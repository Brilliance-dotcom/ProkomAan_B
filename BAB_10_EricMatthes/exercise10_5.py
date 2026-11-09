from pathlib import Path

names = []

while True:
    name = input("Enter a name (or 'q' to quit): ")
    if name == "q":
        break
    names.append(name)

contents = "\n".join(names)

path = Path("guest_book.txt")
path.write_text(contents)