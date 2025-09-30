# Calculate the perimeter of a rectangle given its sides
# Formula: 2l x 2w length -> l and width -> w

length = int(input("Length of the rectangle: "))
width = int(input("Width of the rectangle: "))

perimeter = (2*length) * (2*width)

print("Perimeter rectangle is: ", perimeter)