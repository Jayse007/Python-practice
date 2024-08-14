def prime_number_checker(a):
    if a == 1 or  a == 2 or a == 3 or (a % 2 != 0 and a % 3 != 0):
        print(f"{a} is a prime number")

    else:
        print(f"{a} is not a prime number.")

prime_number_checker(29)

x = [1, 2, 3, 4, 7, 9, 11, 13, 19]

list(map(prime_number_checker, x))