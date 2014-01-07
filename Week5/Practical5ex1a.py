print "\033[1;32mProgram Working\033[1;m"

print "We can work out Distance travelled by multiplying Speed by Time"
speed = float(raw_input("Please enter your speed in mph "))
time = float(raw_input("Please enter the amount of time it took in mins "))
#user is asked to input the speed and time 

distance = speed*(time/60)# the speed is then multiplied by time(which is converted to hrs

print "Your distance travelled in miles was ", distance
#The answer is then  displayed
