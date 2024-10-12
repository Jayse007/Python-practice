# This code is supposed to check a variable and see if there is a valid character "" does not count and " " does not count.

words = input("Please type in a word.")
decider = False
for word in words:
    if word != ("" or " "):
        decider = True
        break
if decider == True:
    print("Arguments found in 'words' variable")

else:
    print("No arguments found 'words' variable")