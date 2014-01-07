print "\033[1;32mProgram Working\033[1;m"

name = raw_input ("What is your name? ")
# I instructed the user to enter their name. the raw input will be assosciate with the
# variable name.

print "Hello %r" % name  
# the program will print the name. %r (raw input) acts as a store within a string. 
# outside the string the store needs to be defined.

word1 = 'The'
word2 = 'cat'
word3 = 'sat'
word4 = 'on'
word5 = 'the'
word6 = 'mat.'
# i have assigned strings to many varibles

print "%s %s %s %s %s %s" % (
	word1, word2, word3, word4, word5, word6
)
# to the print the varables i used the store %s (string. i then identified what varaiables
# are being used.
