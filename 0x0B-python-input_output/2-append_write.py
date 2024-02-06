#!/usr/bin/python3
"""Main module."""


def append_write(filename="", text=""):
    """ A function that  appends a string at the end of a text file (UTF8)
    and returns the number of characters written """
    with open(filename, "a", encoding="utf-8") as file:
        num = file.write(text)
        return num
