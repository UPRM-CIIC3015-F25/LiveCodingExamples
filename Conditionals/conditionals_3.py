'''
Story: 
You are the oracle deciding today’s vibe based on temperature.

Goal: 
	•	Ask for today’s temperature in °F and convert it to C.
	•	If > 30 → “🥵 It’s HOT! Grab some ice cream!”
	•	Else if 15–30 (inclusive) → “😊 Nice weather! Perfect for a walk!”
	•	Else (< 15) → “🥶 Brrr… It’s COLD! Wear a coat!”


End with: “Forecast complete.”



'''
# Formula: (F - 32) x  5/9

temperature = int(input("What is the temperature in Fahrenheit? "))

convert_to_celsius = (temperature - 32) * 5/9

if convert_to_celsius > 30:
    print("It's HOT! Grab some ice cream!")
    print("The temperature was: ", convert_to_celsius)

elif convert_to_celsius >=15 and convert_to_celsius <= 30:
    print("perfect for a walk!")
    print("The temperature was: ", convert_to_celsius)

else:
    print("grab a coat!")
    print("The temperature was: ", convert_to_celsius)









