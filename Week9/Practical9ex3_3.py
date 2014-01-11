print "\033[1;32mProgram Working\033[1;m"

def IsLeapYear(year): # function
   if((year % 4) == 0): # these are all the IF rules for the entered number
      if((year % 100) == 0): # these will check if the year entered can be divided by 4,100,400
         if( (year % 400) == 0):
            return 1
         else:
            return 0
      else:
         return 1
   return 0
 
Year = 0
print "Program to check Leap Year"
print "Enter Year: ", 
Year = input()
if( IsLeapYear(Year) == 1): # if the returned value if 1, it is a leap year.
   print Year, "is a leap year"
else:
   print Year, "is NOT a leap year"
