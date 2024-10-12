import sys, random

wins = 0
losses = 0
ties = 0

while True:
    while True:
        print("Select (r)ock or (p)aper or (s)cissors or (q)uit")
        player = input()

        if player == 'r' or player == 'p' or player =='s' or player == 'q':
            break
        
        print("Please type in 'r' or 's' or 'p' or 'q'")
        
    computer = random.randint(1,3)
    
    if player == 'q':
        sys.exit()

    if computer == 1:
        computer = 'r'
    
    elif computer == 2:
        computer = 'p'
    
    elif computer == 3:
        computer = 's'
    
    

    if player == computer:
        ties += 1
    
    elif player == 'r' and computer == 's':
        wins += 1
     
    elif player == 's' and computer == 'p':
        wins += 1
    
    elif player == 'p' and computer == 'r':
        wins += 1
    
    else:
        losses += 1
    print('computer chose %s' % computer)
    print('You have %s wins %s losses %s ties' % (wins, losses, ties))


    