# 
# Example file for variables
#

# Declare a variable and initialize it
f=0
# print(f)

# re-declaring the variable works
# I first declared f=0 (an integer) and printed it
# I redeclared f="adc" (a string) and printed it
# f="abc"
# print(f)

# ERROR: variables of different types cannot be combined
# This is happening because Python is a strongly typed language
# Python infers a specific type for a value or a variable
# You cannot change the type or combine it with other types
# print("this is a string" + 123)
# print("this is a string " + str(123))

# Global vs. local variables in functions
# Lines 29-31:
# Prints out def and then it prints out 0
# becasue the two fs are different
# Inside the function, the f gets it own local copy
# of whatever variables you declare inside the function
# f=0 is a global variable 
# def someFunction():
#     f="def"
#     print(f)

# By adding global f, it affects the 
# f that is outside the function
def someFunction():
    global f
    f="def"
    print(f)

someFunction()
print(f)

# del statement deletes the definition of 
# a varible that was previously declared
# When I get to the next line an error 
# will occur because that variable is gone
del f
print(f)
