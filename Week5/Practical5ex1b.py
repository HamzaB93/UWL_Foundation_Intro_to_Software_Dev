print "\033[1;32mProgram Working\033[1;m"

print "I can tell you how fast you need to go within a certain time and distance"

distance = float(raw_input("Enter how far you need to go in miles "))
time = float(raw_input("Enter the amount of time you have in mins "))
# user is asked to input time and distance

speed = distance*(time/60)
# distance is multiplied by time (which has been converted to hrs)

print "You need to travel at ", speed, " mph."
print "What are you still doing here, GO!"
# the speed is printed

