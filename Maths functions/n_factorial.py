import sys

def factorial(number):
    result = 1
    for n in range(1, number+1):
        result *= n
    print(result)

while True:
    print("If you choose to stop running this program, type in 0")
    number = int(input())
    if number == 0:
        sys.exit()
    else:
        factorial(number)