# Create a function that counts down from a
# given number to 1, prints "blast off"
# when countdown is finished
# hint: you can use module time, there is a function
# that will print every second called sleep

# 1. Create function called countdown
# 2. Paramater: number
# 3. While Loop: number >= 1

import time

def count_down(number):
    while number >= 1:
        print(number)
        number -= 1
        time.sleep(1)

    print("Blast off!")



count_down(10)