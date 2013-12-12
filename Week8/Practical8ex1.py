import time # importing the time function

counter = 1 # coutn starts from 1
for i in range (0,3): # loop starts 0=1 1=2 2=3 3=GO1
	print counter
	time.sleep(1)
	counter = counter + 1 # will show count as 1, then add 1

print ("GO")

