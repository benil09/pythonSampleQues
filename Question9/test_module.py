# test_module.py
import question9

# Test My_fact function
numbers_for_fact = [5, 3, 0, 7]
factorials = question9.My_fact(*numbers_for_fact)
print(f"Factorials of {numbers_for_fact}: {factorials}")

# Test My_psq function
numbers_for_psq = [4, 16, 18, 25, 30]
perfect_squares = question9.My_psq(*numbers_for_psq)
print(f"Perfect squares from {numbers_for_psq}: {perfect_squares}")