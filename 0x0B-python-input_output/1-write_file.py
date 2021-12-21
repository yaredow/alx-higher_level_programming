#!/usr/bin/python3
"""My return number of lines module"""


def write_file(filename="", text=""):
    with open(filename, mode="w+", encoding='utf-8') as file:
        return file.write(text)