#
# Example file for working with classes
#

# Unlike Java, classes start with a lower case characters
class myClass():
    def method1(self):
        print("myClass method1")

    def method2(self, someString):
        print("myClass method2 " + someString)

class anotherClass(myClass):
    def method1(self):
        myClass.method1(self)
        print("anotherClass method1")

    # method2 is not calling the base class 
    # It is not calling the function in myClass
    def method2(self, someString):
        print("anotherClass method2 ")

def main():
    c = myClass()
    c.method1()
    c.method2("This is a string")

    c2 = anotherClass()
    c2.method1()
    # Even through we are passing in an argument, 
    # the argument is not being used because 
    # we are not calling the inherited method
    c2.method2("This is a different string")

if __name__ == "__main__":
    main()
