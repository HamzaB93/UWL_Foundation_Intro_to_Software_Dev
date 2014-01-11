print "\033[1;32mProgram Working\033[1;m"

count = 1 # count starts at 1
defpass = "changeme" # the desired password is chnageme
attempt = raw_input("Please enter the default password ")
# usr asked to enter password

while attempt != defpass:
	attempt = raw_input("Please enter the default password ")
	count = count + 1
	if count > 4:
		break # count increases when pw is wrong, stops at 4
if attempt == defpass:
	print "Password Accepted, it took you " + str(count) + " attempts"
else:	
	print "Access denied"
