#You can  convert basically every data type can be converted to a boolean value
#Now remember that condition will only be run if it yields a boolean value of "True"
# Below, you can observe some examples.  

no = 'None'

#The value of no is a non-empty string which yields a boolean value of "True", and not inverts a boolean value.
#The result of the condition will be False, hence the code will not print "executed" with not.


if not no:
    print("Executed.......")

#But if you remove the not, the expression will yield a True value. Therefore the cold will execute.


if no:
    print("Postive execution...")