print "\033[1;32mProgram Working\033[1;m" 

import random # importing random function

ran = random.randint (1,10) # using the random function in a range (1-10)

guess = int(raw_input("Try guessing the number between 1-10: ")) 
# the user will guess the number

attempt = 1 # the attempt will start at 0
while guess:
        if guess > ran:
		print "That was higher than I wanted"
	if guess < ran:
		print "That was lower than what I wanted"
	# if statements letting the user know if its high or low 
	guess = int(raw_input("Try guessing again "))
	# after getting it wrong, the user will need to guess again
        attempt = attempt + 1 # 1 will be added to attempt (1)  
	if guess == ran:
        	print "You got it right"       
		break # loop breaks when the user gets it right
print "Well done it took you" , attempt, "attempt(s)" 

