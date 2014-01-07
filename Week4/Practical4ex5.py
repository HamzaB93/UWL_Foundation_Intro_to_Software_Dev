print "\033[1;32mProgram Working\033[1;m"

print "An area of a rectangle is measred by multiplying its height by the width"
print "Area = Height x Width" # quick description of how to calculate area

height = float(raw_input("Please enter a Height in cm ")) # user inputs as float values
width = float(raw_input("Please enter a Width in cm "))

area = height*width
print "Your area is", area, "cm squared"   
#The 2 user inputs are then multiplied together to give the area

print "To calculate volume, we need another value, which is length"
print "We will use your previous numbers, all you need to is add a value for length"
print "Volume = Width x Height x Length" # another description but for volume

length = float(raw_input("Enter your Length "))
volume = area*length #the user input for length is multiplied by identified area
print "Your volume is", volume, "cm cubed"
