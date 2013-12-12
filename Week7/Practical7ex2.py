import random # importing the random number generator function
suit = random.randint (1,4) # suit has been given a random number, ranging 1-4
card_num = random.randint(1,13) # the card number has also been given a random number 1-13 

#if statements which assign a suit name to the the random number
if suit == 1:
	suit_name = "Heart"
if suit == 2:
	suit_name = "Diamond"
if suit == 3:
	suit_name = "Clubs"
if suit == 4:
	suit_name =  "Spades"

print "Your random card is " + str(card_num) + " " + suit_name
# the card suit and number are printed for the user
