import random


card_types = [ 'Clubs ','Hearts', 'Diamonds', 'Spade']
card_values = [number for number in range(1, 11)]
royal_cards = ["Jack", "Queen", "King", "Ace"]

card_values.extend(royal_cards)



chosen_card_type = random.choice(card_types)
chosen_card_value = random.choice(card_values)



print("Your card is %s of %s" % (chosen_card_value, chosen_card_type ))
