print "\033[1;32mProgram Working\033[1;m"

#importing the date function/ module
import datetime 

print "I can tell you how many days you have lived for..."

#These are the raw inputs for the user to enter the date,month and year
date = int(raw_input("Enter the date that you were born on "))
month = int(raw_input("Now enter the month you were born on "))
year = int(raw_input("Finally, enter the year that your were born on "))

#format for date of birth and todays date for thr function
dob = datetime.date(year, month, date) # year month and date are the arguments
today = datetime.datetime.today().date() #  no arguments here, so puts standard time in

print "Todays date is the %d" % today.day
print "The month we are in is %d" % today.month
print "And the year we are in is %d" % today.year
# showing the current date and time with the time function

days = today - dob

print "You have lived a total of ", days.days, "days"
# the days are then presented with the format days.days function

sec = 60 
secondsinhr = 60*sec
secondsinday = 24*secondsinhr
# seconds in a day is then calculated with an functions

print "You have also lived for", days.days*secondsinday, "seconds"
# the days.days calculated is then multiplied by the seconds in a day to give
# how many seconds the user has lived for
