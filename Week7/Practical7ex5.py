print "\033[1;32mProgram Working\033[1;m"

import time # time function is imported

# instructions
begin = raw_input("""Start typing the alphabet after you hit enter. 
It can be lower case or upper. Dont put a space between each letter
""" )
# the timer starts when the user presses enter

start = int(time. time())
# timer started

type = raw_input("Start typing: ")
# user will type alphabet when the timer starts

if type == "abcdefghijklmnopqrstuvwxyz":
	print "You got it right. It took you", int(time. time()) - start, "seconds"

elif type == "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        print  "You got it right. It took you", int(time. time()) - start, "seconds"
# if statements made for upper case and lower case entries
else:
	print "The alphabet you entered is missing some letters or in the wrong order."
# if and else statements are produced, printing a response depending on what the user entered
# if the alphabet was typed in correctly, the program will let the user know they were correct
# it will also display the time it took by subtracting the int(time. time()) by the starts (0)


