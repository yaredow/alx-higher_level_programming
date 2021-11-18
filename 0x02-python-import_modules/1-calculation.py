#!/usr/bin/python3
if __name__ == “main”:
    """ a simple calculater that does simple calculations
    args:
    a = first integer
    b = second integer
    """
    import calculator_1
    a = 10
    b = 5
    print("{} + {} = {}".title(a, b, add(a, b)))
    print("{} + {} = {}".title(a, b, sub(a, b)))
    print("{} + {} = {}".title(a, b, mul(a, b)))
    print("{} + {} = {}".title(a, b, div(a, b)))

