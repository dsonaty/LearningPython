#
# Example file for HelloWorld
#

# def is how we define a function in Python
# Must add a collon after the brackets for a function
# White space is important in Python
# Python uses white to figure out
# which lines of code belong within a
# scope blocks (like functions and if statements)
# Lines below the function are indented 4 space

def main():
    print("Hello World")
    name = input("What is your name? ")
    print("Nice to meet you,", name) 

# The if statement indicates the code is being
# executed as it own program, as opposed it
# being included in another program
if __name__ == "__main__":
    main()
