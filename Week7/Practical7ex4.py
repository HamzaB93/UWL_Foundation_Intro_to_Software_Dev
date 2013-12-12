print "Want to do some maths?"

n1 = float(raw_input("Enter any number you want "))
n2 = float(raw_input("Now enter another number "))
#user is instructed to enter 2 numbers

print "Now pick a function"
# user is shown the list of functions they can pick from
function = raw_input("""
You can select from: 
+  
-  
*  
or /  
Type it in and press enter 
""")# the user must enter one of the funtion

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

