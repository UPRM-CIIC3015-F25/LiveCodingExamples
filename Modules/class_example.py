# Define a function named say_good_morning that takes in string parameter named name,
# and returns a good morning greeting string of the form:
#
# Good morning to you, <name>!
#
#
#  where name is value of the name parameter.
#
# Must include correct capitalization and punctuation.

#name de la funcion: say_good_morning
#parameter: name <- input
# return:  Good morning to you, <name>! <- output

def say_good_morning(name):
    return "Good morning to you, "+name+"!"

name = input("Write your name")
print(say_good_morning(name))