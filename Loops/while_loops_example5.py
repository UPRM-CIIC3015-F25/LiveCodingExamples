# Prompt user to enter password and keep retrying
# until the attempts have reached 3.
# print("Access granted ✅")
# print("Incorrect password ❌")

correct_password = "python"
chances = 3
while chances > 0:
    input_password = input("Enter password: ")

    if input_password == correct_password:
        print("Access granted ✅")
        break

    else:
        chances -= 1
        print("Incorrect password ❌")
else:
    print("Access Denied")