# Convert temperatures from Fahrenheit to Kelvin:
# C = (F − 32) × 5 ⁄ 9
# K = C + 273.15
# F=  (C x 9 / 5) + 32

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def celsius_to_kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def fahrenheit_to_kelvin(fahrenheit):
    celsius = fahrenheit_to_celsius(fahrenheit)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin


example = fahrenheit_to_kelvin(90)
print("What is the temperature in Kelvin:", example)