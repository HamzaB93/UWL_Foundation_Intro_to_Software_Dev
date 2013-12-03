print "An area of a rectangle is measred by multiplying its height by the width"
print "Area = Height x Width"

height = float(raw_input("Please enter a Height "))
width = float(raw_input("Please enter a Width "))

area = height*width
print "Your area is", area  

print "To calculate volume, we need another value, which is length"
print "We will use your previous numbers, all you need to is add a value for length"
print "Volume = Width x Height x Length"

length = float(raw_input("Enter your Length "))
volume = area*length
print "Your volume is", volume
