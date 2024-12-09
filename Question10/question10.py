import random
import pandas as pd

# Step 1: Create lists using list comprehension for 10 students
student_names = ["Student" + str(i) for i in range(1, 11)]  # Student1, Student2, ..., Student10
roll_numbers = [101 + i for i in range(10)]  # Roll numbers 101, 102, ..., 110
mid_sem_marks = [random.randint(40, 100) for _ in range(10)]  # Random marks between 40 and 100

# Step 2: Define the function my_zip to create a list of tuples and check homogeneity
def my_zip(*lists):
    if all(len(lst) == len(lists[0]) for lst in lists):  # Check homogeneity
        return list(zip(*lists))  # Create tuples
    else:
        raise ValueError("Lists are not homogeneous")

# Step 3: Use my_zip to combine the lists into a list of tuples
student_data = my_zip(student_names, roll_numbers, mid_sem_marks)
print("List of tuples (Name, Roll No, Mid Sem Marks):")
print(student_data)

# Step 4: Define the my_sort function to sort the list of tuples
def my_sort(data, key_index=1, reverse=False):
    """
    Sorts the data (list of tuples) based on a given key (index of tuple) and order.
    
    Parameters:
    - data: The list of tuples to be sorted
    - key_index: The index of the tuple to sort by (0 for Name, 1 for Roll No, 2 for Marks)
    - reverse: Boolean value indicating whether to sort in reverse order (descending) or not
    
    Returns:
    - Sorted list of tuples.
    """
    return sorted(data, key=lambda x: x[key_index], reverse=reverse)

# Step 5: Sort the student data by mid-sem marks (index 2)
sorted_by_marks = my_sort(student_data, key_index=2, reverse=True)
print("\nSorted by Mid Sem Marks (Descending):")
print(sorted_by_marks)

# Step 6: Create a DataFrame from the student data
df = pd.DataFrame(student_data, columns=["Name", "Roll No", "Mid Sem Marks"])

# Step 7: Add two new columns: Assignment Marks and End Sem Marks with random values between 40 and 100
df["Assignment Marks"] = [random.randint(40, 100) for _ in range(10)]
df["End Sem Marks"] = [random.randint(40, 100) for _ in range(10)]

# Step 8: Calculate the total of Mid Sem, End Sem, and Assignment Marks
df["Total Marks"] = df["Mid Sem Marks"] + df["End Sem Marks"] + df["Assignment Marks"]

# Step 9: Display the DataFrame
print("\nDataFrame with Assignment and End Sem Marks:")
print(df)

# Step 10: Save the DataFrame as a CSV file
df.to_csv("student_data.csv", index=False)
print("\nData saved to 'student_data.csv'.")