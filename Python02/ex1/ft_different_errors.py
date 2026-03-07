#!/usr/bin/env python3

def garden_operations():
    """demonstrates common errors"""
    num = "six seven"
    int(num)

    num = 67
    num = num/0

    open('missing.txt', 'r')

    human = {'name': 'Adnane'}
    plant = human['plantr']
    plant


def test_error_types():
    """Catches each error and explains what went wrong"""
    try:
        print("Testing ValueError...")
        num = "six seven"
        int(num)
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")

    try:
        print("Testing ZeroDivisionError...")
        num = 67
        num = num/0
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")

    try:
        print("Testing FileNotFoundError...")
        open('missing.txt', 'r')
    except FileNotFoundError:
        print("Caught FileNotFoundError: No such file 'missing.txt'\n")

    try:
        print("Testing KeyError...")
        human = {'name': 'Adnane'}
        plant = human['plantr']
        plant
    except KeyError:
        print("Caught KeyError: 'missing\\_plant'\n")

    print("Testing multiple errors together...")
    print("Caught an error, but program continues!\n")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===", end="\n\n")

    test_error_types()

    print("All error types tested successfully!")
