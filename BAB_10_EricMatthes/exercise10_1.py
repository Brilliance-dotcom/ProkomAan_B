from pathlib import Path

path = Path("learning_python.txt")

# Cara 1: baca seluruh isi file sekaligus
contents = path.read_text()
print(contents)

print("---")

# Cara 2: simpan baris-baris ke dalam list, lalu loop satu per satu
lines = contents.splitlines()
for line in lines:
    print(line)