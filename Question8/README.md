Here is a Python program that defines a function unique_elements() which takes two sets as input and returns a new set containing elements that are unique to each set (i.e., elements that are only in one of the sets and not in both):


Explanation:

	1.	symmetric_difference():
	   •	The symmetric_difference() method returns a set containing elements that are in either set1 or set2, but not in both. This gives us the unique elements in each set.
	2.	Test Case:
	  •	set1 = {1, 2, 3, 4, 5}
	  •	set2 = {4, 5, 6, 7, 8}
	  •	The symmetric difference will return the elements that are only in one of the sets: {1, 2, 3, 6, 7, 8}.

This output shows the elements that are unique to each set, excluding the common elements between the two sets.