spam = 0

#Expectations: This is meant to print out "Hello, user" 6 times. WHY?
#If statement is executed once no matter the conditions as far as its condition returns True
#While statement continues to run a piece of code as long as its condition(s) is met. 
#With the while statement one needs to be wary of infinity loops.


if spam <5:
    print("Hello, user.")

while spam < 5:
    print("Hello, user")
    spam += 1 