#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)

  # Check for item existence and type
  print("Item exists: " + str(path.exists("textfile.txt")))
  print("Item is a file: " + str(path.isfile("textfile.txt")))
  print("Item is a directory: " + str(path.isdir("textfile.txt")))
  
  # Work with file paths
  print("Item path: " + (path.realpath("textfile.txt")))
  # Split function separates the file name from the path
  print("Item path and name: " + str(path.split(path.realpath("textfile.txt"))))

  # Get the modification time
  # The function getmtime mean get modification time of the file.
  t = time.ctime(path.getmtime("textfile.txt"))
  print(t)
  # Does the same as the above but using datetime
  print(datetime.datetime.fromtimestamp(path.getmtime('textfile.txt')))

  # Calculate how long ago the item was modified
  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print("It has been " + str(td) + " since the file was modified")
  print("Or, " + str(td.total_seconds()) + " seconds") 

if __name__ == "__main__":
  main()
