# and
# Prompt: Print whether 5 is greater than 0 AND 5 is less than 10

print("and example")
print(5 > 0 and 5 < 10)



# ----------------------------------------------------------------------------------------------------------
# or
# Prompt: Print whether 7 is less than 3 OR 7 is greater than 5

print("or example")
print (7 < 3 or 7 > 5)



# ----------------------------------------------------------------------------------------------------------
# not
# Prompt: Print whether NOT(2 equals 3)

print("not example")
print(not 2==3)



# ----------------------------------------------------------------------------------------------------------
# Combining logical operators
# or & and
# Prompt: Print whether (4 is even AND greater than 2) OR equal to 10

print("or & and example")
print((4%2==0 and 4 > 2) or 4 == 10)


# ----------------------------------------------------------------------------------------------------------
# and & not
# Prompt: Print whether a two words are equal AND NOT equal to "hello"

print("and & not example")
print('hello'=='hello' and not 'goodbye'=='hello')


# ----------------------------------------------------------------------------------------------------------
# or & not
# Prompt: Print whether NOT(3 < 2) OR 10 < 5


print("or & not example")
print(not(3<2) or 10 < 5)


# ----------------------------------------------------------------------------------------------------------
# and, or & not
# Prompt: Print whether (6 is positive AND less than 10) OR NOT divisible by 3


print("and, or & not example")
print((6>0 and 6<10) or not 6/3)