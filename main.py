"""
This is the main module to test importing and using custom packages.
Try pylint main.py to test for static code analysis.
"""

import mymath

def main():
    """ Main module """
    print("This is the beginning of the main file.\n")

    print("2 + 2 =", mymath.basic.add(2,2))
    print("h + 2 =", mymath.basic.add("h",2))
    print()
    print("5 - 2 =", mymath.basic.subtract(5,2))
    print("? - 2 =", mymath.basic.subtract("?",2))
    print()
    print("4 * 3 =", mymath.basic.multiply(4,3))
    print("4 * t =", mymath.basic.multiply(4,"t"))
    print()
    print("9 / 3 =", mymath.basic.divide(9,3))
    print("9 / 0 =", mymath.basic.divide(9,0))
    print("0 / 3 =", mymath.basic.divide(0,3))
    print("p / 3 =", mymath.basic.divide('p',3))

    print("\nThis is the end of the main file.")

if __name__ == "__main__":
    main()
