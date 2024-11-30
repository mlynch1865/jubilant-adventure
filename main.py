"""
This is the main module to test importing and using custom packages.
Try pylint main.py to test for static code analysis.
"""

import mymath

def main():
    """ Main module """
    print("This is the beginning of the main file.\n")

    print("2 + 2 =", mymath.basic.add(2,2))
    
    print("\nThis is the end of the main file.")

if __name__ == "__main__":
    main()
