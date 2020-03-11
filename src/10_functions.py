# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

# Read a number from the keyboard
num = input("Enter a number: ")

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE
try:
    num = int(num)
    if(num !=0):
        if(num %2==0):
            print("EVEN")
        else:
            print("ODD")
    else:
        print("Input can't be zero or null")
except ValueError:
    print("Only number is accepted")