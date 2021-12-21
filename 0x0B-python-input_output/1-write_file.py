#!/usr/bin/python3
"""My file reading module"""


def write_file(filename="", text=""):
    """writes text to a string"""
    with open(filename, mode="w", encoding="utf-8") as f:
        f.write("string")

