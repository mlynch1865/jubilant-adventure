def add(a,b):
    """
    Adds two numbers together. Ensures both can be integers.
    """
    try:
        a = int(a)
        b = int(b)
        return a + b
    except ValueError:
        print("Must enter two numbers.")
        return None

def subtract(a,b):
    """
    Subtracts a second number from a first. Ensures both can be integers.
    """
    try:
        a = int(a)
        b = int(b)
        return a - b
    except ValueError:
        print("Must enter two numbers.")
        return None

def multiply(a,b):
    """
    Returns the product of two numbers. Ensures both can be integers.
    """
    try:
        a = int(a)
        b = int(b)
        return a * b
    except ValueError:
        print("Must enter two numbers.")
        return None

def divide(a,b):
    """
    Divides number a first number by a second. Ensures both can be integers and the second is not zero.
    """
    try:
        a = int(a)
        b = int(b)
        return a / b
    except ValueError:
        print("Must enter two numbers.")
        return None
    except ZeroDivisionError:
        print("The dividend (second number) cannot be zero.")
        return None
