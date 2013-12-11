name = raw_input("What is your name? ") # User is asked to input their name

age = int(raw_input("How old are you " +name+ "? "))
# the variable is added as a string in the new question, which askes the user to 
# input age

newage = age + 1
# The age they will be next year is calculated by adding 1 to curentt age

print "Oh, so your on your next birthday your going to be" ,newage
# the new age is then printed
