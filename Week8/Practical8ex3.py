print "\033[1;32mProgram Working\033[1;m"

# user is asked to enter a number
number = int(raw_input("Enter any number: "))

fact = 1

while number: # loop 
	fact = fact*number # the number entered will be timesed by 1 
	number = number - 1 # 1 taken away from the entered number and looped

print "Your factorial for the number you enetered is", fact
# the factorial for the entered number is printed
