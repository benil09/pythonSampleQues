You can follow these steps to achieve the desired functionality in Python:
	1.	Input Start and End Number: Take two inputs for the start and end of the range.

	2.	Generate NumPy Array: Create a NumPy array of numbers in that range with a step of 1.

	3.	Form a Square Matrix B: The number of elements should be a perfect square for a square matrix to be formed. If the length of the generated array is not a perfect square, you can discard extra elements or adjust the range.

	4.	Extract Prime and Non-Prime Numbers: Extract the prime numbers and non-prime numbers into two separate arrays.

	5.	Create Diagonal Matrices: Construct diagonal matrices with the prime and non-prime numbers placed on the diagonals.

Explanation:

	1.	Prime Check: The is_prime() function checks whether a given number is prime or not. Numbers less than 2 are automatically considered non-prime.

	2.	Input Handling: The program prompts the user to input the start and end numbers. It creates a NumPy array from this range using np.arange(start, end + 1).

	3.	Forming a Square Matrix: The array is reshaped into a square matrix using arr.reshape(square_size, square_size), where square_size is the square root of the array length. If the total number of elements is not a perfect square, the excess elements are discarded.

	4.	Extracting Primes and Non-Primes: The array is filtered to separate prime and non-prime numbers into two lists, B1 (prime) and B2 (non-prime).

	5.	Diagonal Matrices:
	   •	B11 is a zero matrix where prime numbers from B1 are placed along the diagonal.
	   •	B22 is similarly created for non-prime numbers from B2.


Notes:

	1.	If the range contains fewer than the required elements to fill the square matrix, the program will adjust by discarding excess numbers.

	2.	The prime check works efficiently by testing divisibility up to the square root of each number.

	3.	If you enter a range with numbers that result in no primes or no non-primes, the diagonal matrices will contain zeros accordingly.

