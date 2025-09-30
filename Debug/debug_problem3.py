points = 0

question1_answer = input("What's the capital of Puerto Rico: ")

if question1_answer == "San Juan":
    print("Correct!")
    points = 5
    print(f"You now have a total of {points} points.\n")
else:
    print("Sorry, that's not correct.\n")

question2_answer = input("Where is UPRM located?: ")

if question2_answer == "Mayaguez":
    print("Correct!")
    points += 5
    print(f"You now have a total of {points} points.\n")
else:
    print("Sorry, that's not correct.\n")

question3_answer = input("What is the intro to programming class code?: ")

if question3_answer == "CIIC3015":
    print("Correct!")
    points += 5
else:
    print("Sorry, that's not correct.\n")
print(f"Your final total is {points} points.\n")
