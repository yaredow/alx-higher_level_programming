#!/usr/bin/python3
"""My read file module"""


def read_file(filename=""):
    """Read a text file"""
    with open(filename, encoding='utf-8') as f:
        file = f.read()
        print(file, end="")
