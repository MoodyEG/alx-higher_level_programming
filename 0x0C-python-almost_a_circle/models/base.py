#!/usr/bin/python3
"""Base module."""
import json
import csv
import turtle
import time


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
        attrs = []
        if list_objs is not None:
            for i in range(len(list_objs)):
                attrs.append(list_objs[i].to_dictionary())
        jattrs = cls.to_json_string(attrs)
        with open(filename, 'w') as file:
            file.write(jattrs)

    @staticmethod
    def from_json_string(json_string):
        """ Load data from a JSON string """
        if json_string is None or json_string == "":
            json_string = "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an instance based on a dictionary """
        if cls.__name__ == "Rectangle":
            dummy = cls(10, 10)
        if cls.__name__ == "Square":
            dummy = cls(10)
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

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Save the content of a list to a CSV file """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for data in list_objs:
                if cls.__name__ == "Rectangle":
                    writer.writerow([data.id, data.width, data.height,
                                     data.x, data.y])
                if cls.__name__ == "Square":
                    writer.writerow([data.id, data.size,
                                     data.x, data.y])

    @classmethod
    def load_from_file_csv(cls):
        """ Load objects from a CSV file
        had AI help for that"""
        filename = "{}.csv".format(cls.__name__)
        if cls.__name__ == "Rectangle":
            keys = ['id', 'width', 'height', 'x', 'y']
        elif cls.__name__ == "Square":
            keys = ['id', 'size', 'x', 'y']
        data = []
        try:
            with open(filename, 'r') as file:
                readerlist = list(csv.reader(file))
            datalist = []
            for rl in readerlist:
                datadict = {}
                for row in enumerate(rl):
                    datadict[keys[row[0]]] = int(row[1])
                datalist.append(datadict)
            for i in range(len(datalist)):
                data.append(cls.create(**datalist[i]))
        except FileNotFoundError:
            pass
        return data

    @staticmethod
    def draw(list_rectangles, list_squares):
        """ Draw all shapes on the screen """
        screen = turtle.Screen()
        screen.bgcolor("black")
        pen = turtle.Turtle()
        pen.penup()
        pen.color("blue")
        for rectangle in list_rectangles:
            pen.pendown()
            for i in range(2):
                pen.forward(rectangle.width)
                pen.right(90)
                pen.forward(rectangle.height)
                pen.right(90)
            pen.penup()
            pen.forward(rectangle.width + 24)
        pen.color("purple")
        for square in list_squares:
            pen.pendown()
            for i in range(4):
                pen.forward(square.size)
                pen.right(90)
            pen.penup()
            pen.forward(square.size + 24)
        time.sleep(2)
        screen.bye()
