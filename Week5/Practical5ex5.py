print "\033[1;32mProgram Working\033[1;m"

import time # time function is imported

begin = raw_input("Lets see how good you are at guessing 10 seconds. Press enter the start the timer")
# raw input instructing the user to press enter

start =int( time. time())
# start of the counter

end = raw_input("Press enter when you think 10 seconds has elapsed")
# instruction of the user, the count has started

print "You guessed", int(time.time()) - start, "seconds." 
# the time that the user hit enter is displayed
