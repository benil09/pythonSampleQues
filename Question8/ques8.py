def unique_elements(set1, set2):
    # Using symmetric_difference() to find unique elements in each set
    return set1.symmetric_difference(set2)

# Test the function
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Call the function with the test sets
result = unique_elements(set1, set2)

print("Unique elements in both sets:", result)