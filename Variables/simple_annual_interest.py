# Savings account 1 year earnings at simple annual interest
# Interest = P x R x T
# P = Principal amount (the beginning balance).
# R = Interest rate (usually per year, expressed as a decimal). %
# T = 1

principal_amount =  int(input("Principal amount: "))
rate = int(input("Rate of interest in %, example 3 will be 3%: "))

interest =  principal_amount * (rate/100) * 1

print("Savings account 1 year earnings at simple annual interest: ", interest+principal_amount)


# Savings account n year earnings at simple annual interest
# Interest = P x R x T
# P = Principal amount (the beginning balance).
# R = Interest rate (usually per year, expressed as a decimal). %
# T = Number of time periods (generally one-year time periods)

principal_amount =  int(input("Principal amount: "))
rate = int(input("Rate of interest in %, example 3 will be 3%: "))
time_period = int(input("Time period: "))

interest =  principal_amount * (rate/100) * time_period

print("Savings account n year earnings at simple annual interest: ", interest+principal_amount)
