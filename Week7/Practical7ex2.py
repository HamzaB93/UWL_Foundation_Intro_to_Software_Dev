import random
suit = random.randint (1,4)
card_num = random.randint(1,13)

if suit == 1:
	suit_name = "Heart"
if suit == 2:
	suit_name = "Diamond"
if suit == 3:
	suit_name = "Clubs"
if suit == 4:
	suit_name =  "Spades"

print "Your random card is " + str(card_num) + " " + suit_name
