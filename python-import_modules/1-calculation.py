#!/usr/bin/python3

a = 10
b = 5

def add(x, y):
    """Return the sum of x and y"""
    return x + y

def sub(x, y):
    """Return the difference of x and y"""
    return x - y

def mul(x, y):
    """Return the product of x and y"""
    return x * y

def div(x, y):
    """Return the integer division of x by y"""
    return x // y  # integer division

if __name__ == "__main__":
    print("Addition: {} + {} = {}".format(a, b, add(a, b)))
    print("Subtraction: {} - {} = {}".format(a, b, sub(a, b)))
    print("Multiplication: {} * {} = {}".format(a, b, mul(a, b)))
    print("Division: {} / {} = {}".format(a, b, div(a, b)))
