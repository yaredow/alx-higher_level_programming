#!/usr/bin/python3
"""My file reading module"""


def write_file(filename="", text=""):
    """writes text to a string"""
    with open(filename, encoding="utf-8") as f:
        return f.write("string")

