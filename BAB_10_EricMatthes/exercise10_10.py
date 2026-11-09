from pathlib import Path

filenames = ["alice.txt"]

for filename in filenames:
    path = Path(filename)
    try:
        contents = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"Sorry, the file {filename} is missing.")
    else:
        count_the = contents.lower().count("the")
        count_the_space = contents.lower().count("the ")
        print(f"{filename}:")
        print(f"  'the' appears about {count_the} times.")
        print(f"  'the ' (with a space) appears {count_the_space} times.")