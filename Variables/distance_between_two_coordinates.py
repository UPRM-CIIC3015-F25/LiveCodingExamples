import math

# Distance between two points given their coordinates (x, y)
# Formula: d = √((x₂ - x₁)² + (y₂ - y₁)²)

x1 = int(input("Enter the first x coordinate: "))
y1 = int(input("Enter the first y coordinate: "))
x2 = int(input("Enter the second x coordinate: "))
y2 = int(input("Enter the second y coordinate: "))

distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

print("Distance between two coordinates is: ", distance)