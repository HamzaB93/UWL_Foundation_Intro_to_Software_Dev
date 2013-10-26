my_name = 'Hamza Bhatti' #words must have single quotes
my_age = 19 #this doesnt have a single quote
my_height = 74 #inches
my_weight = 140 #pounds or lbs
my_eyes = 'Brown'
my_teeth = 'White'
my_hair = 'Black'
#Everything i have typed so far is a variable


print "Let's talk about %s." % my_name
print "He's %d inches tall," % my_height
print "He's %d pounds heavy," % my_weight
print "Actually that's not too heavy,"
print "He's got %s eyes and %s hair," % (my_eyes, my_hair)
#Everything in the brackets has to be in order
print "His teeth are usually %s," % my_teeth

#the next line shows that the order of the %d needs to match the order in the brackets
print "If I add %d, %d, and %d I get %d." % (
	my_age, my_height, my_weight, my_age + my_height + my_weight)
