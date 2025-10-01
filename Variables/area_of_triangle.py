import math

# Area of triangle given lengths of its three sides (Heron’s formula)
# Semi-perimeter formula: (a + b + c) / 2
# Area Formula: √(s x ( s - a) x (s - b) x (s - c))

a = int(input("Enter the first side of the triangle: "))
b = int(input("Enter the second side of the triangle: "))
c = int(input("Enter the third side of the triangle: "))

s = (a + b + c) / 2

area = math.sqrt(s * (s - a) * (s - b) * (s - c))


print("The area of the triangle is: ", math.ceil(area))