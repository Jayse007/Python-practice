import random, sys

print("You are to type two numbers. The first number should not be higher than the second number.")
print("If you wish to quit press ctrl + c")


while True:
    try:
        a = int(input())
        b = int (input())
        
        if  b-a < 2:
            print("Please follow the instructions")
            continue

        magic_number = random.randint(a,b)
        print("Guess the number")


       
        for guess in range(3):
           print("type in 0 to quit")
           player_guess = int(input())
           
           if player_guess == 0:
              sys.exit()
           if player_guess < magic_number:
             print("Your number is too low")
               
           elif player_guess > magic_number:
             print("Your number is too high")
               
           else:
             print("You are correct.")

    except:
        print("Please follow the instructions")
        continue
               
        