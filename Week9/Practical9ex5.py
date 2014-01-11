print "\033[1;32mProgram Working\033[1;m"

def marktograde(a): # creating function for the first grade
	if a >= 80: # if statements for the score entered
		print "M1 grade: A"
	elif a >= 70:
		print "M1 grade: B"
	elif a >= 60:
		print "M1 grade: C"
	elif a >= 50:
		print "M1 grade: D"
	elif a >= 40:
		print "M1 grade: E"
	elif a <= 39:
		print "M1 grade: U"
mark = float(raw_input("Enter the percentage mark for module1: "))
marktograde (mark)# user input grade, the function is called upon, and will return grade
                       
# this function is the same as the previous but for the second module grade
def marktograde2(b):
        if b >= 80:
                print "M2 grade: A"
        elif b >= 70:
                print "M2 grade: B"
        elif b >= 60:
                print "M2 grade: C"
        elif b >= 50:
                print "M2 grade: D"
        elif b >= 40:
                print "M2 grade: E"
	elif b <= 39:
                print "M2 grade: U"


mark2 = float(raw_input("Enter the second percentage mark for module2: "))
marktograde2(mark2)

def overall(c): # this function compares the two grades and gives average
        if c >= 80:
                print "Overall grade: A"
        elif c >= 70:
                print "Overall grade: B"
        elif c >= 60:
                print "Overall grade: C"
        elif c >= 50:
                print "Overall grade: D"
        elif c >= 40:
                print "Overall grade: E"
        elif c <= 39:
                print "Overall grade: U"

overallmark = (mark+mark2)/2 # working out average for the 2 scores
overall(overallmark) # the last function is called upon
