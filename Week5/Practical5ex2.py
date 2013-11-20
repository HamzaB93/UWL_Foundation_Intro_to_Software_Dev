daysperweek = 7 #days
hoursperday = 24 #hours
minutesperhour = 60 #mins

print """ #Describing the premise
We have 7 days a week
Each day lasts 24 hours
in each hour we have 60 minuts
"""
print "To calculate how many minuts there are in a week we must do the following:"

print "First we need to find out how many minutes there are in a day."
print "We will multiply the minutes in one hour by the hours in a day."  
print "Which 60 x 24, which gives us:" 
minsaday = minutesperhour*hoursperday #formula and answer
print minsaday

print "All we need to do now is multiply our minuts in a day which is by the days of the week, which is 7"  
print "Our minuts in a week is:" #formual and answer below
minsaweek = minsaday*daysperweek
print minsaweek
