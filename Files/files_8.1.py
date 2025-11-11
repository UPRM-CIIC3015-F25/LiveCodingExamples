# UPRM CIIC 3015 Fall 2025
# Lecture 8: Files and Exceptions

# Live Coding Example 8_1

# Write "Hello World" to file in a single line
def write_hello_world(filename):
    pass

# write_hello_world("hello_world.txt")

# Read "Hello World" from file
def read_hello_world(filename):
    pass

# print(read_hello_world("hello_world.txt"))


# Write integers 0 to n-1 to file one per line
def write_int_range(filename, n):
    f = open(filename, "w")
    for i in range(n):
        f.write(str(i)+"\n")
    f.close()

#write_int_range("integers.txt", 20)

# Read and return list of integers 0 to n from
# file one per line
def read_int_range(filename, n):
    pass

# print(read_int_range("integers.txt", 20))

def dump_file(filename):
    f = open(filename, "r")
    for line in f:
        print(line.strip())

dump_file("integers.txt")

# Return sum of all integers in file
def sum_ints_from_file(filename, n):
    pass

# print(sum_ints_from_file("integers.txt", 20))


# Write integers 0 to n to file single line comma separated
# 10 numbers per line
def write_int_range_csv(filename, n):
    f = open(filename, "w")
    counter = 0
    for i in range(n):
        f.write(str(i))
        counter += 1
        if counter % 10 == 0:
            f.write("\n")
        else:
            f.write(",")
    f.close()

write_int_range_csv("integers.csv", 100)



# write_int_range_csv('excel.csv', 100)

# Read integers 0 to n from file single line comma separated
def read_int_range_csv(filename):
    pass

# read_int_range_csv('excel.csv')

def read_matrix(filename):
    pass

#print(read_matrix("numbers.csv"))



