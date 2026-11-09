from random import randint


class Die:
    """Representasi sebuah dadu."""

    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        """Cetak angka acak antara 1 dan jumlah sisi dadu."""
        print(randint(1, self.sides))


print("Rolling a 6-sided die 10 times:")
die_6 = Die()
for roll in range(10):
    die_6.roll_die()

print("\nRolling a 10-sided die 10 times:")
die_10 = Die(10)
for roll in range(10):
    die_10.roll_die()

print("\nRolling a 20-sided die 10 times:")
die_20 = Die(20)
for roll in range(10):
    die_20.roll_die()