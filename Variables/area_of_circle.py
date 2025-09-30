# Area of a circle given its radius
# Formula: A=πr^2

import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * math.pow(radius, 2)

print("The area of a circle is: ", area)