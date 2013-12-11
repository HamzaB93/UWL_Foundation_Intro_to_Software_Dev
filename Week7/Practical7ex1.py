print "You have to be a certain age for to be able to vote "
age = int (raw_input ("Please type in your age "))
# the user is asked to enter their age

if age < 18 :
	print "Sorry you cant vote"

if age > 17 :
	print "You can vote" 
# two if statements have been created. if the user is less than 18
# the user cannot vote, if above 17, they can vote
