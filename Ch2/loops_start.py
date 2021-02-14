#
# Example file for working with loops
# Python only has two ways of doing loops, while and for
#

def main():
  x = 0

  # define a while loop
  # while (x<5):
    # print (x)
    # x = x + 1

  # define a for loop
  # Python's for loops are called iterators 
  # The for loop will start at 5 and stop at 9,
  #  the number before 10
  # for x in range(5, 10):
  #   print(x)

  # use a for loop over a collection
  # days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  # for d in days:
  #   print (d)

  # use the break and continue statements
  # break statement is used to break the execution
  # of a loop, if a condition is met
  # continue statement skips the rest of the 
  # loop for that particular iteration
  # for x in range(5,10):
  #   # if (x==7): break
  #   if (x % 2 == 0): continue
  #   print(x)

  # using the enumerate() function to get index 
  # Python does not use an index variable 
  # enumerate will iterate over this collection like loop 
  # normally would, but in addition to returning the value 
  # of the item being looked at, it also returns a value 
  # that is the index fo the item in question
  days=["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
  for i,d in enumerate (days):
    print (i, d)

if __name__ == "__main__":
  main()
