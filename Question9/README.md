To create a module named my_module with the functions My_fact() and My_psq(), you can follow the steps below. The module will contain the logic for calculating factorials and identifying perfect squares from a variable number of arguments passed to the functions. Additionally, we’ll call both functions from another script to demonstrate their usage.


Explanation:

	•	My_fact():

	  •	This function takes a variable number of arguments (*args), calculates the factorial for each valid integer passed to it (non-negative integers), and returns a list of factorials.

	  •	It uses an internal factorial() function to calculate the factorial of each number by multiplying the numbers from 1 to n.

	•	My_psq():
	  •	This function checks whether each number passed is a perfect square and returns a list of all perfect squares. The is_perfect_square() function is used to check if the number has a square root that is an integer.

2. Create a script to call the functions from my_module:


3. Explanation:

	•	Test My_fact(): We pass a list of numbers ([5, 3, 0, 7]) to calculate their factorials.
	•	Test My_psq(): We pass a list of numbers ([4, 16, 18, 25, 30]) to find which ones are perfect squares.


5. How to Use:

	1.	Save the my_module.py and test_module.py files in the same directory.
	2.	Run test_module.py by executing it from the terminal or IDE.


Final Notes:

	•	This structure allows you to encapsulate the logic for factorial calculation and perfect square detection in a reusable module (my_module.py).
	•	You can pass as many arguments as needed to both functions, and the functions will handle them appropriately, returning a list of results.