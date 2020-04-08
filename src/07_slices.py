"""
Python exposes a terse and intuitive syntax for performing 
slicing on lists and strings. This makes it easy to reference
only a portion of a list or string. 

This Stack Overflow answer provides a brief but thorough
overview: https://stackoverflow.com/a/509295

Use Python's slice syntax to achieve the following:
"""

a = [2, 4, 1, 7, 9, 6]

arr=[]
# Output the second element: 4:
print(f"The second element in {a} is: {a[-5]}")

# Output the second-to-last element: 9
print(f"The second-to-last element in {a} is: {a[-2]}")

# Output the last three elements in the array: [7, 9, 6]
print(f"The last three elements in the array {a} is: {a[3:6]}")

# Output the two middle elements in the array: [1, 7]
print(f"The two middle elements in the array {a} is: {a[2:4]}")

# Output every element except the first one: [4, 1, 7, 9, 6]
print(f"Output of every element in {a} except the first one is: {a[1:]}")

# Output every element except the last one: [2, 4, 1, 7, 9]
print(f"Output of every element in {a} except the last one is: {a[:-1]}")

# For string s...

s = "Hello, world!"

# Output just the 8th-12th characters: "world"

print(s[7:12])