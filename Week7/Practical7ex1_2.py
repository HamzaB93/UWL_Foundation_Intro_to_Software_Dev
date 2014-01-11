print "\033[1;32mProgram Working\033[1;m"

print "You have to be a certain age for to be able to vote "
age = int (raw_input ("Please type in your age: "))
# the user is asked to enter their age

if age >= 18 : # if the age is 18 and over, they can vote
        print "You can vote."

else: # otherwise they are not allowed
	print "You can't vote. Sorry."



