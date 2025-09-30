# Prompt user to enter password and keep retrying
# until the password matches.

correct_password = "helloworld"
user_input = ""

while user_input != correct_password:
    user_input = input("Enter password: ")
    if user_input == correct_password:
        print("Correct password!")
    else:
        print("Wrong password!!")
