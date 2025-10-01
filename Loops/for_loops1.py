# Print all the numbers from 0 to N

# def print_numbers(end):
#     for num in range(end+1): # range(0,101)
#         print(num)
#
# print(print_numbers(100))

text = "hello"
for i in range(len(text)):
   for j in range(i + 1, len(text)):
       if text[i] == text[j]:
           print(f"Duplicate: {text[i]} at {i} and {j}")


