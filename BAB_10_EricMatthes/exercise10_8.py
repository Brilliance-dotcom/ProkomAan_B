from pathlib import Path

filenames = ["cats.txt", "dogs.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} is missing.")
    else:
        print(f"Names in {filename}:")
        print(contents)