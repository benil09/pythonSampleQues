import numpy as np

# Function to create a diagonal matrix from an array
def create_diagonal_matrix(array, size):
    diag_matrix = np.zeros((size, size), dtype=int)
    for i in range(min(len(array), size)):
        diag_matrix[i, i] = array[i]
    return diag_matrix

# Step 1: Take input from the user for start and end numbers
start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

# Step 2: Create the NumPy array from start to 2*end, incremented by 2
arr = np.arange(start, 2 * end + 1, 2)

# Step 3: Check if the length of the array is a perfect square to form a square matrix
length = len(arr)
square_size = int(np.sqrt(length))  # The size of the square matrix

# Adjust the array to fit a square matrix if necessary (discard extra elements)
arr = arr[:square_size * square_size]
M = arr.reshape(square_size, square_size)

print("\nSquare Matrix M:")
print(M)

# Step 4: Take input for the non-zero number 'n'
n = int(input("\nEnter a non-zero number 'n' to filter elements: "))

# Step 5: Create arrays A1 and A2 based on divisibility by 'n'
A1 = arr[arr % n == 0]  # Elements divisible by n
A2 = arr[arr % n != 0]  # Elements not divisible by n

print("\nArray A1 (Divisible by n):")
print(A1)

print("\nArray A2 (Not divisible by n):")
print(A2)

# Step 6: Create diagonal matrices A11 and A22
A11 = create_diagonal_matrix(A1, square_size)
A22 = create_diagonal_matrix(A2, square_size)

print("\nDiagonal Matrix A11 (A1 on diagonal):")
print(A11)

print("\nDiagonal Matrix A22 (A2 on diagonal):")
print(A22)