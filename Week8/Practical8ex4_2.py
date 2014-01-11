print "\033[1;32mProgram Working\033[1;m"

sentence = [str(raw_input("Type in your sentence and I will count how many words there are: "))]
# the sentence variable has a raw_input in list format []

for item in sentence: # the loop starts here
        print len(item.split()) # the len function count the words in the string entered
	break

newsentence = raw_input("Enter another sentene and I will show you it in reverse: ") # instruction

print  newsentence, " In reverse it is: " ,newsentence[::-1] # ::-1 means count the string in reverse
# the reverse of the string entered is printed



