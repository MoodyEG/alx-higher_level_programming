#!/usr/bin/python3
"""Main module."""


def from_json_string(my_str):
    """ A function that returns an object
    represented by a JSON string """
    import json
    return json.loads(my_str)
