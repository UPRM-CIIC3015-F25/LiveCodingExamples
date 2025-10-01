import math

# UPRM CIIC 3015 Fall 2025
# Lecture 5: Lists, Strings and Tuples
# Live Coding Examples
# Instructors: Karelys López and Bienvenido Vélez

# PART A: EXAMPLES WITH LISTS

# Example #1 ------------------------------------------------
# Function print_list(l) that prints all elements in list l
def print_list(l):
    for e in l:
        print(e)

# Tests
print(print_list([1,2,3,4,5,6])) # Should print [1,2,3,4,5,6]

# Example #1b ------------------------------------------------
# Function print_list_with_pos(l) that prints all elements in list l together
# with their positions
def print_list_with_pos(l):
    for e in range(len(l)):
        print(f"Element in position {e} is {l[e]}")

# Tests
print(print_list_with_pos([1,2,3,4,5,6]))


# Example #2 ------------------------------------------------
# Function sum_of_list(l) that returns the sum of all the numbers in a list l

def sum_of_list(numbers):
    suma = 0
    for e in numbers:
        suma += e
    return suma

# Tests
print(sum_of_list([1,2,3,4,5])) # Should print 10



# Example #2b ------------------------------------------------
# Function sum_of_list_at_even_pos(l) that returns the sum of all the numbers
# in a list l at even positions
def sum_of_list_at_even_pos(numbers):
    suma = 0
    for index in range(len(numbers)):
        if index % 2 == 0:
            suma += numbers[index]
    return suma

# Tests
#print(sum_of_list_at_even_pos([1,2,3,4,5,6])) # Should print 4 (1 + 3)


# Example #3 ------------------------------------------------
# Function average_of_list(l) that returns the average of all the numbers in
# list l.  Returns -1 if the list is empty.

def average_of_list(l):
    if len(l)==0:
        return -1
    suma = 0
    for e in l:
        suma += e
    return suma / len(l)

# Tests
# print(average_of_list([1,2,3,4])) # Should print 2.5
# print(average_of_list([])) # Should print -1

# Example #4
# Function largest_number(l) that returns the largest number with a list l of
# numbers.  Returns None if the list is empty.
def largest_number(l):
    max_so_far = l[0]
    for next_number in l[1:]:
        if next_number > max_so_far:
            max_so_far = next_number
    return max_so_far

# Example 4b: Homework: Try to return the position of the largest



# Example #5 ------------------------------------------------
# Function number_exists(n, l) that returns True if a number n exist is a
# list l and False otherwise.

def number_exists(n, l):
    for e in l:
        if e == n:
            return True
        else:
            return False

#Test cases
#number_exists(5, [1,2,3,4,5],)

# Example #6
# Function find_number(n, l) that determines the position of the first
# occurrence of a number nwithin a list l or -1 if it doesn't exist.
def find_number(n,l):
    for idx in range(len(l)):
        if l[idx] == n:
            return idx
        return -1


# Example #7
# Function filter_list_evens(l) that returns a new list containing all even
# numbers in list l

def filter_list_evens(l):
    result = []
    for e in l:
        if e % 2 == 0:
            result.append(e)
    return result
# Tests
# print(filter_list_evens([1,2,3,4,5,6])) # Should print [2, 4, 6]


# Example #8
# Function replace_negatives(l, n) that takes a list of numbers (int's or
# float's) and returns a new list with all negative numbers replaced with
# number n.
def replace_negatives(l, replacement):
    result = []
    for e in l:
        if e<0:
            result.append(replacement)
        else:
            result.append(e)
    return result

# Problem 8b (Homework) Write a version of replace_negatives that modifies
# the original list instead of creating a new list.






