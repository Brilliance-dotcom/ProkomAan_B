from random import sample

pool = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d", "e"]

my_ticket = [3, 7, "b", 9]

attempts = 0
won = False

while not won:
    winning_ticket = sample(pool, 4)
    attempts += 1

    # set dipakai supaya urutan item tidak berpengaruh
    if set(winning_ticket) == set(my_ticket):
        won = True

print(f"My ticket: {my_ticket}")
print(f"The loop had to run {attempts} times to win.")