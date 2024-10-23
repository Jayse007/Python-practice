x = type(1)

def max_num(*num):
    y = num[0] 
    
    for i in num:
        if type(i) != x:
            raise Exception("Please input an integer data type.")
        if i > y:
            y = i
    print(y)

max_num(2,5,3, 15 , 6, 8, 4)

print(3 * "5")