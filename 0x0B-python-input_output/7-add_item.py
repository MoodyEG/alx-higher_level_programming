#!/usr/bin/python3
"""Main module."""


import sys

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

pylist = []
try:
    pylist = load_from_json_file("add_item.json")
except FileNotFoundError:
    pass

for arg in sys.argv[1:]:
    pylist.append(arg)

save_to_json_file(pylist, "add_item.json")
