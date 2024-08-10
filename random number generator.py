import random

SID = random.randrange(1, 6)
existing = [1, 2, 3]

while SID in existing:
    SID = random.randrange(1,6)
print(SID)
