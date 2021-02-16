#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  # The open function takes two arguments. The first is the 
  # file to operation on. The second is the kind of access you 
  # want. w stand for write access and the + mean to create the 
  # file if it doesn't exist alread.
  # f = open("textfile.txt", "w+")

  # Open the file for appending text to the end
  # The "a" parameter means to append data to the end of the 
  # file instead of overwriting all the existing content 
  # that's already in there.
  # f = open("textfile.txt", "a")

  #  The "r" parameter means read the file.
  f = open("textfile.txt", "r")

  # write some lines of data to the file
  # "\r\n" is style fo rnew line
  # for i in range(10):
  #   f.write("This is link " + str(i) + "\r\n")

  # close the file when done
  # Closing the file after you are done.
  # f.close()
  
  # Open the file back up and read the contents
  # The reason for f.mode ="r" is to make sure that 
  # the file wsa successfully opened. If it isn't 
  # open, there is nothing to read.
  # if f.mode == "r":
  #   contents = f.read()
  #   print(contents)

  # For reading the contents of a file line by line 
  # use the readline or readlines function.
  if f.mode =="r":
    fl = f.readlines()
    for x in fl:
      print(x)

if __name__ == "__main__":
  main()
