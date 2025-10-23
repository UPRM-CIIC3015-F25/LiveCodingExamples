# PART C: EXAMPLES WITH MULTI-DIMENSIONAL LISTS (Matrices)

# UPRM CIIC 3015 Spring 2025
# Lecture 5: Strings and Lists

# Live Coding Example 7
# Multi-dimensional lists


# Create an M x N 2d List of int's
# Let M = 4 and N = 3
M = 3
N = 3

matrix = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# Print the 2D List in Table Form Using Nested Loops
# The simplest way is to use NESTED LOOPS
def print_by_rows(matrix, M, N):
    for r in range(M):
        for c in range(N):
            print(matrix[r][c])

print_by_rows(matrix,M,N)

# Print the Transposed 2D List in Table Form Using Nested Loops
def print_transposed(matrix, N, M):
    for c in range(N):
        for r in range(M):
            print(matrix[r][c])

# print_transposed(matrix, N, M)

# Print the Mirror Image of a 2D List
def print_mirror(matrix, M, N):
    for r in range(M-1,-1,-1):
        for c in range(N-1,-1,-1):
            print(matrix[r][c])

# print_mirror(matrix, M, N)

# Calculate Mean of All int's in a 2D List
def matrix_average(matrix, M, N):
    sum=0;
    for r in range(M):
        for c in range(N):
            sum += matrix[r][c]
    return sum / (M*N)


def average_column(matrix, M, N, c):
    sum = 0;
    for r in range(M):
        sum += matrix[r][c]
    return sum / M

print(f"The average of row {2} of matrix is {average_column(matrix,M,N, 1)}")



# Add two 2D Lists
def add_matrices(matrix1, matrix2, R, C):
    result = []
    for r in range(R):
        next_row = []
        for c in range(C):
            next_row.append(matrix1[r][c] + matrix2[r][c])
        result.append(next_row)
    return result

m1 = [[1,2],[3,4]]
m2 = [[5,6],[7,8]]

sum_matrix = add_matrices(m1, m2, 2, 2)

print('Done')

