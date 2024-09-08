import random

outcomes = ["H", "T"]

possibilities = [random.choice(outcomes) for i in range(0, 20)]

print(possibilities)