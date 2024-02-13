#!/usr/bin/python3
""" Base Test module """
from models.base import Base
import unittest
from models.rectangle import Rectangle
import json


class test_baseinit(unittest.TestCase):
    """ Testing base class """
    def test_1_base(self):
        """ Testing base with no args """
        a = Base()
        self.assertEqual(a.id, 1)

    def test_2_base(self):
        """ Testing base with one arg """
        a = Base(24)
        self.assertEqual(a.id, 24)
        a = Base(-12)
        self.assertEqual(a.id, -12)

    def test_3_base(self):
        """ Testing private attributes """
        a = Base()
        with self.assertRaises(AttributeError):
            print(self.__nb_objects)

    def test_4_base(self):
        """ Testing many arguments """
        with self.assertRaises(TypeError):
            a = Base(1, 1, 1)

    def test_5_base(self):
        """ Testing to_json_string """
        d = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        ds = Base.to_json_string([d])
        self.assertIsInstance(ds, str)
        self.assertEqual(ds, '[{"x": 2, "width": 10, "id": 1,\
                         "height": 7, "y": 8}]')
        d1 = None
        ds1 = Base.to_json_string(d1)
        self.assertEqual(ds1, '[]')
        d2 = {}
        ds2 = Base.to_json_string([d2])
        self.assertEqual(ds2, '[{}]')

    def test_6_base(self):
        """ Testing from_json_string """
        s = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        ds = Base.from_json_string(s)
        self.assertIsInstance(ds, list)
        dl = [{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]
        self.assertEqual(ds, dl)
        s1 = None
        ds1 = Base.from_json_string(s1)
        self.assertEqual(ds1, [])
        s2 = ""
        ds2 = Base.from_json_string(s2)
        self.assertEqual(ds2, [])

    def test_7_base(self):
        """ Testing create """
        a = Rectangle(1, 2, 3, 4, 5)
        dic = a.to_dictionary()
        a1 = Rectangle.create(**dic)
        self.assertEqual(a1.__str__(), "[Rectangle] (5) 3/4 - 1/2")
        self.assertIsNot(a, a1)

    def test_8_base(self):
        """ Testing save_to_file """
        a = Rectangle(1, 2, 3, 4, 5)
        a1 = Rectangle(1, 1, 1, 1, 1)
        Rectangle.save_to_file([a, a1])
        with open("Rectangle.json", "r") as file:
            jd = json.dumps([a.to_dictionary(), a1.to_dictionary()])
            self.assertEqual(jd, file.read())
        Rectangle.save_to_file(None)
        with open("Rectangle.json", "r") as file:
            self.assertEqual("[]", file.read())
        Rectangle.save_to_file([])
        with open("Rectangle.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_9_base(self):
        """ Testing load_from_file """
        a = Rectangle(1, 2, 3, 4, 5)
        Rectangle.save_to_file([a])
        l0 = Rectangle.load_from_file()
        self.assertIsInstance(l0, list)
        self.assertEqual(l0[0].__str__(), "[Rectangle] (5) 3/4 - 1/2")
        Rectangle.save_to_file(None)
        l1 = Rectangle.load_from_file()
        self.assertIsInstance(l1, list)
        self.assertEqual(len(l1), 0)
        Rectangle.save_to_file([])
        l2 = Rectangle.load_from_file()
        self.assertIsInstance(l2, list)
        self.assertEqual(len(l1), 0)
