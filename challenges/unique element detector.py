# The point of this code is to detect a number that has no duplicate in the 
# NOTE: All other elements are meant to have only one duplicate or else the code will produce unwanted results.

def scan_list(elements):
    result = 0
    
    for element in elements:
        if isinstance(element, int):
            result ^= element
        
        else:
            raise Exception("This is not a number. Please type in a number")
    
    if result not in elements:
        return "Are you incapable of reading comments or do you have an inherent problem."
         
    return result

elements = [8, 4, 4, 5, 6, 7, 6, 5, 7]

print(scan_list(elements))


