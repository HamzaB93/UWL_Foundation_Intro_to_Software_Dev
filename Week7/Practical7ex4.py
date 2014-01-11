print "\033[1;32mProgram Working\033[1;m"

print "Want to do some maths?"

n1 = float(raw_input("Enter any number you want "))
#user is instructed to enter a number

# user is shown the list of functions they can pick from
function = raw_input("""Now pick a function. You can select from: 
+  -  *  or /  . Type it in and press enter 
""")# the user must enter one of the funtion

n2 = float(raw_input("Now enter another number ")) # user put 2nd number

# variables are created using the functions in the list
add = n1 + n2
sub = n1 - n2
mult = n1 * n2
divi = n1 / n2

# if statements are created which will display an answer depending on
# which function was entered. the answers are taken from the variables
# above (add sub etc)
if function == "+":	
	print "Your answer is" , add 
elif function == '-':
	print "Your answer is" , sub
elif function == '*':
	print "Your answer is" , mult 
elif function == '/':
	print "Your answer is" , divi

