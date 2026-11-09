from pathlib import Path

path = Path("pi_string.txt")
contents = path.read_text()

pi_string = ""
for line in contents.splitlines():
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))