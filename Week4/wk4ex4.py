#I am specifing with a variable how many cars there will be
cars = 350

#I am now defining how much space there is in the car
space_in_a_car = 2.0

#Stating how many drivers there are
drivers = 40

#Showing how many passengers there are
passengers = 100

#I am now making a variable with a formula for cars not driven
cars_not_driven = cars - drivers

#The next variable are the cars driven which matches the drivers
cars_driven = drivers

#This variable shows the carpool capacity by multiplying the cars driven with the space in the car
carpool_capacity = cars_driven * space_in_a_car

#Next is the average passangers per car by using another formula
average_passengers_per_car = passengers / cars_driven


print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "THere will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
