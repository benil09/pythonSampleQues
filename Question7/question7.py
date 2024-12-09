def sort_list(string_list):
    # Sorting the list of strings based on their length using a lambda function
    string_list.sort(key=lambda x: len(x))
    return string_list

# Test the function
strings = ["apple", "banana", "kiwi", "mango", "cherry"]
sorted_strings = sort_list(strings)

print("Sorted list based on string length:")
print(sorted_strings)