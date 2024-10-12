wounds = ["Abrasions", "Bruise", "Burns", "Scars"]

def wounds_addition(wounds, wound_name):
    wounds.append(wound_name)

wounds_addition(wounds , "strain")

print(wounds)




c = ["youtube"]
d = [c]

print(id(c))
print(id(d))
c.extend(("King", "Queen", "Jack"))

print(id(c))
print(d)
#Be very careful when dealing with lists as this can cause unwanted behaviour.
#In this code, assigning c variale as an element of 