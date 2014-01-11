print "\033[1;32mProgram Working\033[1;m"

import random # importing the random number generator function
suit = random.randint (1,4) # suit has been given a random number, ranging 1-4
card_num = random.randint(1,13) # the card number has also been given a random number 1-13

#if statements which assign a suit name and type to the the random numbers
if card_num == 1:
	suit_type = "Ace"
if card_num == 11:
	suit_type = "Jack"
if card_num == 12:
	suit_type = "Queen"
if card_num == 13:
	suit_type = "King"
if card_num == 2:
	suit_type = "2"
if card_num == 3:
	suit_type = "3"
if card_num == 4:
	suit_type = "4"
if card_num == 5:
	suit_type = "5"
if card_num == 6:
	suit_type = "6"
if card_num == 7:
	suit_type = "7"
if card_num == 8:
	suit_type = "8"
if card_num == 9:
	suit_type = "9"
if suit == 1:
        suit_name = "Heart"
if suit == 2:
        suit_name = "Diamond"
if suit == 3:
        suit_name = "Clubs"
if suit == 4:
        suit_name =  "Spades"

print "Your random card is " + suit_type + " " + suit_name
# the card suit and number are printed for the user

