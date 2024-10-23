name = 'hope'
name2 = name



#Strings are immutable, so changing the value of name2 variable will not affect the name variable +
#although it is a refernce of the same object

print(name is name2)


#A list is a mutable data type, so any pointer referencing a list will share the same id as long as +
#the reference connection is not broken

l = ['josh', 'marie', 'magnus']
m = l

m.append('Theresa')
print(m is l)



#This is an example of the reference breaking. Although they were sharing the same id berfore, m is no longer referencing +
#the m variable because it is now pointing to a new object rather than l's object.


m = []

print(l)
print(m)

#for better understanding, create two new lists or reassign l and m with empty lists i.e [] +
#you will notice that they have different ids even though they are equal to each other.
#This happens because each time you create a new empty list, you create a new object entirely.

m = []
l = []

print(m is l)
print(m == l)



l = ['Josh', 'Marie', 'Magnus']
m = l

l = []

print(m is l)
print(m)
print(l)

