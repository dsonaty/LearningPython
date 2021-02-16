#
# Example file for working with filesystem shell methods
#
import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile

def main():
  # make a duplicate of an existing file
  if path.exists("textfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("textfile.txt")

    # let's make a backup copy by appending "bak" to the name
    # dst is destination 
    dst = src + ".bak"

    # copy over the permissions, modification times, and other info
    # copy function only copies over the contents of the file
    # shutil.copy(src, dst)
    # # copystat copies over things like modification time 
    # # and other metadata associate with the file
    # shutil.copystat(src, dst)

    # rename the original file
    # os.rename("textfile.txt", "newfile.txt")

    # now put things into a ZIP archive
    # Compress everything within the directory 
    # root_dir, tail = path.split(src)
    # shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    # with statement in Python is used in exception handling to 
    # make the code cleaner and much more readable. It simplifies 
    # the management of common resources like file streams. 
    with ZipFile("testzip.zip", "w") as newzip:
      newzip.write("textfile.txt")
      newzip.write("textfile.txt.bak")

if __name__ == "__main__":
  main()
