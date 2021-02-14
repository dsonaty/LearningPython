#
# Example file for working with conditional statements
#


def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    # if x = y the first condition (x < y) will evaluate to false 
    # therefore the second condition (else) will evaluate to true
    # This is the reason we have to add the elif condition
    # Python does NOT use switch and uses elif as a substitute
    if (x < y):
        st = "x is less than y"
    elif (x == y):
        st = "x is the same as y"
    else:
        st = "x is greater than y"

    print(st)

    # conditional statements let you use "a if C else b"
    st = "x is less than y" if (x<y) else "x is greater than or equal to y"

    print(st)  

if __name__ == "__main__":
    main()
