# For the exercise, look up the methods and functions that are available for use
# with Python lists.

x = [1, 2, 3]
y = [8, 9, 10]

# For the following, DO NOT USE AN ASSIGNMENT (=).

# Change x so that it is [1, 2, 3, 4]
# YOUR CODE HERE
print(f"current Items in x: {x}")
x.append(4)
print(f"Updated Items in x:")
print(x)

# Using y, change x so that it is [1, 2, 3, 4, 8, 9, 10]
# YOUR CODE HERE
print(f"current Items in x: {x}")
x.extend(y)
print(f"Updated Items in x:")
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 10]
# YOUR CODE HERE
print(f"current Items in x: {x}")
x.remove(8)
print(f"Updated Items in x:")
print(x)

# Change x so that it is [1, 2, 3, 4, 9, 99, 10]
# YOUR CODE HERE
print(f"current Items in x: {x}")
x.insert(5,99)
print(f"Updated Items in x:")
print(x)

# Print the length of list x
# YOUR CODE HERE
print(f"Length of x list is: {len(x)}")
# Print all the values in x multiplied by 1000
# YOUR CODE HERE
def itemMul(x):
    print(f"Multiplying each Item in x by 1000")
    for item in x:
        print(f"{item} *1000 =\"{item*1000}")
itemMul(x)