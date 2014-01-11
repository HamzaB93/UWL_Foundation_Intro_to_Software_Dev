print "\033[1;32mProgram Working\033[1;m"

def maximum(a,b): # defining the function
	max2 = [a,b] # the twi variables are put in a list
	print "The largest number out your entry was", max(max2)
	# max is the function which compares the values and gives the largest

print "Enter two number and I will give you the largest out of them."
n1 = float(raw_input("Enter your first number: ")) # user asked to enter 2 values
n2 = float(raw_input("Enter your second number: "))

maximum(n1,n2) # n1 n2 are put put into the function. a=n1, b=n2


def maximum_3(q,r,s): #new function
	max3 = [q,r,s] # variables put in a list
	print "The largest out of the three numbers is", max(max3)
	# max function used again

print "Now we will see the largest number out of 3 entries"
number1 = float(raw_input("Enter a number: "))
number2 = float(raw_input("Enter your second number: "))
number3 = float(raw_input("Now your last number: "))
# user asked for 3 numbers this time

maximum_3(number1,number2,number3)
# the function is called for, number1=q, number2=r, number3=s 
