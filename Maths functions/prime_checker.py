def prime_number_checker(a):
    prime_number = True
    for i in range(2, a):
        if a % i ==0:
            prime_number = False
            return prime_number
        
        
    return prime_number 
        
            
        

print(prime_number_checker(29*29))



