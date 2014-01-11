print "\033[1;32mProgram Working\033[1;m"

hrsspnt = int(raw_input("So tell me, how long do you spend on the computer? "))
# user is asked to enter how long they spend on the computer

if hrsspnt <= 3:
	print "Sounds reasonable."

elif hrsspnt == 4:
	print "Do you have time for anything else?"

elif hrsspnt >= 5:	
	print "Dude you need a life"
# if statements give a differnt response to the user depending on what they enter

print "Thats all folks"
