#!/bin/user/python3
"""My read file module"""


def read_file(filename=""):
    """Read a text file"""
    with open("filename, 'r', encoding='utf-8'") as f:
        text = f.read()
        print(text, end="")
