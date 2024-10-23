import sys

def collatz(number):
    if number % 2 == 0:
        print(number // 2)
    
    else:
        print((number*3) + 1)

while True:
    print("Please type in a number")
    try:
        number_input = int(input())
        if number_input == 1:
            sys.exit()
    except ValueError:
        continue

        
    collatz(number_input)