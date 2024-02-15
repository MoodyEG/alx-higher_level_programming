#!/usr/bin/python3
""" Main Module """


def append_after(filename="", search_string="", new_string=""):
    """ A function that inserts a line of text to a file,
    after each line containing a specific string """
    with open(filename) as file:
        lines = file.readlines()
    modified_lines = []
    for line in lines:
        if search_string in line:
            modified_lines.append(line + new_string)
        else:
            modified_lines.append(line)
    with open(filename, "w") as file:
        file.writelines(modified_lines)
