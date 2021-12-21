# !/usr/bin/python3
"""number_of_lines module"""


def number_of_lines(filename=""):
    """to read # of lines"""
    with open(filename, mode="w+", encoding="utf-8") as content:
        content.write("text")