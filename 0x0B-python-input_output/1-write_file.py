#!/usr/bin/python3
"""Main module."""


def write_file(filename="", text=""):
    """ A function that writes a string to a text file (UTF8)
    and returns the number of characters written """
    with open(filename, "w", encoding="utf-8") as file:
        num = file.write(text)
        return num
