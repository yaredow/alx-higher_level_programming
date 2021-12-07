#!/usr/bin/python3
"""My square module"""


def __init__(self, size=0):
    """Define a square"""
    self.__size = size
try:
    type(size) = int
except TypeError:
    print("size must be an integer")
try:
    if size < 0:
except ValueError:
    print("size must be >= 0")
        
