#!/usr/bin/python3
"""Main module."""


def to_json_string(my_obj):
    """ A function that returns the JSON
    representation of an object (string) """
    import json
    return json.dumps(my_obj)
