#!/usr/bin/python3
"""Base module."""
import json


class Base:
    """ Our Base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initializing Base """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Convert list of dictionaries into a JSON string """
        if list_dictionaries is None:
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ Save the content of the list in a file """
        filename = "{}.json".format(cls.__name__)
        if list_objs is None:
            pass
        else:
            attrs = []
            for i in range(len(list_objs)):
                attrs.append(list_objs[i].to_dictionary())
            jattrs = cls.to_json_string(attrs)
            with open(filename, 'w') as file:
                file.write(jattrs)

    @staticmethod
    def from_json_string(json_string):
        """ Load data from a JSON string """
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance based on a dictionary """
        dummy = cls(10, 10)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Load objects from a file and returns them in a list"""
        filename = "{}.json".format(cls.__name__)
        datalist = []
        try:
            with open(filename, 'r') as file:
                filelist = cls.from_json_string(file.read())
            for obj in range(len(filelist)):
                datalist.append(cls.create(**filelist[obj]))
        except FileNotFoundError:
            pass
        return datalist
