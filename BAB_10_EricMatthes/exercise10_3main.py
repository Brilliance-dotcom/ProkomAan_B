from pathlib import Path

path = Path("pi_string.txt")
contents = path.read_text()

for line in contents.splitlines():
    print(line)