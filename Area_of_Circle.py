import math
radius = float(input("Input the radius of the circle: "))
area = math.pi*radius**2
print("The area of the circle with radius " +str(radius)+" is: "+str(area))

filename = input("Input the Filename: ").split(".")
print ("The extension of the file is : " +filename[-1])
