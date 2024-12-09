import numpy as np

# Step 1: Get the shape of arrays A1 and A2 from the user
rows1 = int(input("Enter the number of rows for the first array (A1): "))
cols1 = int(input("Enter the number of columns for the first array (A1): "))
rows2 = int(input("Enter the number of rows for the second array (A2): "))
cols2 = int(input("Enter the number of columns for the second array (A2): "))

# Step 2: Generate two random 2D arrays with values between 0 and 100 (you can adjust the range)
A1 = np.random.randint(0, 100, size=(rows1, cols1))
A2 = np.random.randint(0, 100, size=(rows2, cols2))

print("\nArray A1:")
print(A1)

print("\nArray A2:")
print(A2)

# Step 3: Construct A11 by selecting elements of A1 divisible by 3 but not divisible by 4
A11 = A1[(A1 % 3 == 0) & (A1 % 4 != 0)]

# Step 4: Construct A22 by selecting elements of A2 divisible by 2 and 3
A22 = A2[(A2 % 2 == 0) & (A2 % 3 == 0)]

# Step 5: Check if either A11 or A22 is empty and continue if they are
while A11.size == 0 or A22.size == 0:
    print("\nEither A11 or A22 is empty. Re-generating arrays...\n")
    A1 = np.random.randint(0, 100, size=(rows1, cols1))
    A2 = np.random.randint(0, 100, size=(rows2, cols2))
    print("New Array A1:")
    print(A1)
    print("\nNew Array A2:")
    print(A2)
    
    # Recompute A11 and A22
    A11 = A1[(A1 % 3 == 0) & (A1 % 4 != 0)]
    A22 = A2[(A2 % 2 == 0) & (A2 % 3 == 0)]

# Step 6: Join A11 and A22 to form a single dimensional array
combined_array = np.concatenate((A11, A22))

# Step 7: Construct the largest possible square matrix from the combined array
# Find the largest perfect square number less than or equal to the length of the combined array
square_size = int(np.floor(np.sqrt(combined_array.size)))
square_matrix = combined_array[:square_size * square_size].reshape(square_size, square_size)

print("\nLargest possible square matrix constructed from the combined array:")
print(square_matrix)