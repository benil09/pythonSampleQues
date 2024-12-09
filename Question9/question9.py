# my_module.py

# Function to calculate factorial of numbers
def My_fact(*args):
    def factorial(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact
    
    result = []
    for num in args:
        if isinstance(num, int) and num >= 0:
            result.append(factorial(num))
        else:
            result.append(None)  # To handle invalid inputs like negative numbers
    return result

# Function to find perfect squares
def My_psq(*args):
    def is_perfect_square(n):
        if n < 0:
            return False
        i = 1
        while i * i <= n:
            if i * i == n:
                return True
            i += 1
        return False
    
    result = []
    for num in args:
        if isinstance(num, int) and num >= 0:
            if is_perfect_square(num):
                result.append(num)
        else:
            result.append(None)  # Handle invalid inputs
    return result