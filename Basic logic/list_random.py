import random

team_mates = ['Henry', 'Lebron', 'Harden', 'Stephen', 'Durant', 'Kyrie']


#Each time this program is run, it selects a random team mate as the winner of the raffle draw
#My money is on Harden


raffle_winner = random.choice(team_mates)
print(raffle_winner)

lineup_shuffle = random.shuffle(team_mates)

print(team_mates)

