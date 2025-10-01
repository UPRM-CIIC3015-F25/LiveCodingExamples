import math

# Convert temperatures from Fahrenheit to Kelvin:
# C = (F − 32) × 5 ⁄ 9
# K = C + 273.15
# F=  (C x 9 / 5) + 32

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit

def distance_two_coordinates(x1,y1,x2,y2):
    distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
    return distance