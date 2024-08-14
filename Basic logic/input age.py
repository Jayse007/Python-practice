while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
        if age < 1:
           print('Please enter a positive number.')
           continue
        break
    except:
        print('Please use numeric digits.')
        continue
    
   
print(f'Your age is %d.' % age)
