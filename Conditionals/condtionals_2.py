''' 
Story:
Student is trying to save for an upcoming big purchase in a year,
the student will put an amount of money in a savings accounts with
a simple annual interest of 3% to achieve the goal amount they want.
Return if they achieve the goal or not

Reminder:
Savings account 1 year earnings at simple annual interest
Interest = P x R x T
P = Principal amount (the beginning balance).
R = Interest rate (usually per year, expressed as a decimal). %
T = 1

Goals:
	•	Ask the user for the amount they will put in the savings account.
	•	What else do we need?

End with: “Savings Achieved!” or "Not enough money!"
'''

goal = int(input("What is your goal? "))
principal_amount = int(input("What is your principal amount?"))

interest = 0.03*1*principal_amount

total = interest + principal_amount

if total >= goal:
    print("Amount achieved! The amount was", total)

else:
    print("Not enough money! Missing: ", goal-total)



