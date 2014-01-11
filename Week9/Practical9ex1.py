print "\033[1;32mProgram Working\033[1;m"

def countstring(mystring): # function created
	for item in mystring: # for loop
		print "Words in your sentence: ", len(item.split())
		# len function used to count the words in the string
		break
        

mystring = [raw_input("Enter a sentence an I will count how many words there are: ")] 
# user entering a number

countstring(mystring)# caling on the function above
 
 
