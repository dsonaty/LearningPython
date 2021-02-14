#
# Example file for working with functions
# Functions are small blocks of code
# Functions themselves are objects that can be 
# passed around to other pieces of Python code
#

# define a basic function
# Functions are defined by the def keyword, 
# followed by a name for the function, 
# then open and close parens
# ending with a colon, which indicates 
# the start fo the function's scope block
def func1():
    print("I am a function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)

# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# func1()
# The function is being called inside the print function 
# then the outer print statement executes
# since the functin does not return a value 
# Python evaluates the return value the Python constant of none 
# and prints the string representation of that
# print (func1())
# The function itself is not being executed because 
# we did not including the prarentheses which would call it 
# the value of the fucntion definition is printed instead
#print(func1)

# func2(10,20)
# print (func2(10,20))
# print (cube(3))

# Calling the function power but not giving it a 
# value for x so x is going to default to one
# print (power(2))
# Calling the function power with num equal to two 
# and the power is equal to three
# print (power(2,3))
# Reversing the order in which the arguments are called
# print (power(x=3, num=2))

# You can combine a variable argument list with a set of 
# fomal aurguments, but keep in mind that the variable 
# argument list always has to be the last paramenter
print (multi_add(10, 4, 5, 10, 4))
