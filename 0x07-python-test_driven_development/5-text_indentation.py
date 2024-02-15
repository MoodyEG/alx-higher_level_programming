#!/usr/bin/python3
""" Main Module """


def text_indentation(text):
    """ A function that prints a text with 2 new lines
    after each of these characters: ., ? and : """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = text[:]
    for sep in ".?:":
        s = result.split(sep)
        result = ""
        for line in s:
            line = line.strip(" ")
            if result == "":
                result = line + sep
            else:
                result += "\n\n" + line + sep
    print(result[:-3], end='')
