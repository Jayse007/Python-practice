while True:
    print('Enter your age:')
    age = input()
    try:
        age = int(age)
        break
    except:
        print('Please use numeric digits.')
        continue
    if age < 1:
        print('Please enter a positive number.')
        continue
   
print(f'Your age is {age}.')
