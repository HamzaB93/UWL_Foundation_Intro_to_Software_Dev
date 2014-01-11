print "\033[1;32mProgram Working\033[1;m"

class Calculations(object): # Creating class
	def _init_ (self, number1, number2,number3): # initialising class		
		self.number1 = number1 # self.variables, 
		self.number2 = number2 # ensuring variables are associated with the class
		self.number3 = number3
	def sum (self, number1, number2, number3): # creating sum function
		print "Your sum is: ", number1+number2+number3 # adding all numbers
	def average (self, number1, number2, number3):# creating average function
		print "Your average is: ", float((number1+number2+number3)/3)
	def maximum (self, number1, number2, number3): # function withing a function: max
		print "The largest number you entered was: ", max(number1, number2, number3)
	def minimum (self, number1, number2, number3): # function withing a function: min
		print "The smallest number you entered was: ", min(number1, number2, number3)
print "We are going to do some maths"

Calculations = Calculations() # calling on the class
number1 = int(raw_input("Please enter your first number: ")) # user inputs the 3 numbers
number2 = int(raw_input("Now enter your second number: "))
number3 = int(raw_input("Finally enter your first number: "))

Calculations.sum(number1, number2, number3) # class and the objects
Calculations.average(number1, number2, number3)
Calculations.maximum(number1, number2, number3)
Calculations.minimum(number1, number2, number3)
