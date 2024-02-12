#!/usr/bin/python3
from models.rectangle import Rectangle
import unittest
from contextlib import redirect_stdout
import io


class test_rectangleinit(unittest.TestCase):
    """ Testing rectangle class """
    def test_1_rectangle(self):
        """ Testing if attributes are set correctly in rectangle"""
        a = Rectangle(10,20,30,40,50)
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 20)
        self.assertEqual(a.x, 30)
        self.assertEqual(a.y, 40)
        self.assertEqual(a.id, 50)

    def test_2_rectangle(self):
        """ Testing error for negative arguments """
        with self.assertRaises(ValueError):
            a = Rectangle(-1, 1, 1, 1)
        with self.assertRaises(ValueError):
            a = Rectangle(1, -1, 1, 1)
        with self.assertRaises(ValueError):
            a = Rectangle(1, 1, -1, 1)
        with self.assertRaises(ValueError):
            a = Rectangle(1, 1, 1, -1)

    def test_3_rectangle(self):
        """ Testing error for missing arguments """
        with self.assertRaises(TypeError):
            a = Rectangle()

    def test_4_rectangle(self):
        """ Testing error for too many arguments """
        with self.assertRaises(TypeError):
            a = Rectangle(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    def test_4_rectangle(self):
        """ Testing error for TypeError """
        with self.assertRaises(TypeError):
            a = Rectangle("Hi", 1, 1, 1)
        with self.assertRaises(TypeError):
            a = Rectangle(1, "Hi", 1, 1)
        with self.assertRaises(TypeError):
            a = Rectangle(1, 1, "Hi", 1)
        with self.assertRaises(TypeError):
            a = Rectangle(1, 1, 1, "Hi")

    def test_5_rectangle(self):
        """ Testing setter """
        a = Rectangle(1, 1, 1, 1)
        a.width = 10
        a.height = 20
        a.x = 30
        a.y = 40
        self.assertEqual(a.width, 10)
        self.assertEqual(a.height, 20)
        self.assertEqual(a.x, 30)
        self.assertEqual(a.y, 40)

    def test_6_rectangle(self):
        """ Testing setter type errors """
        a = Rectangle(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            a.width = "Hi"
        with self.assertRaises(TypeError):
            a.height = []
        with self.assertRaises(TypeError):
            a.x = {}
        with self.assertRaises(TypeError):
            a.y = ()

    def test_6_rectangle(self):
        """ Testing setter value errors """
        a = Rectangle(1, 1, 1, 1)
        with self.assertRaises(ValueError):
            a.width = -1
        with self.assertRaises(ValueError):
            a.height = -1
        with self.assertRaises(ValueError):
            a.x = -1
        with self.assertRaises(ValueError):
            a.y = -1

    def test_7_rectangle(self):
        """ Testing area """
        a = Rectangle(10, 20)
        self.assertEqual(a.area(), 200)

    def test_8_rectangle(self):
        """ Testing display """
        a = Rectangle(1, 1, 1, 1)
        expected_output = "\n #\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            a.display()
            output = buf.getvalue()
        self.assertEqual(output, expected_output)

    def test_9_rectangle(self):
        """ Testing __str__ method """
        a = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(a.__str__(), "[Rectangle] (5) 3/4 - 1/2")

    def test_10_rectangle(self):
        """ Testing update """
        a = Rectangle(1, 1, 1, 1, 1)
        a.update(89)
        self.assertEqual(a.id, 89)
        a.update(89, 2)
        self.assertEqual(a.width, 2)
        a.update(89, 2, 3)
        self.assertEqual(a.height, 3)
        a.update(89, 2, 3, 4)
        self.assertEqual(a.x, 4)
        a.update(89, 2, 3, 4, 5)
        self.assertEqual(a.y, 5)

    def test_11_rectangle(self):
        """ Testing private attributes """
        a = Rectangle(1, 2, 3, 4, 5)
        with self.assertRaises(AttributeError):
            print(a.__width)
        with self.assertRaises(AttributeError):
            print(a.__height)
        with self.assertRaises(AttributeError):
            print(a.__x)
        with self.assertRaises(AttributeError):
            print(a.__y)

    def test_12_rectangle(self):
        """ Test bad args with update """
        a = Rectangle(1, 1, 1, 1, 1)
        with self.assertRaises(ValueError):
            a.update(1, -1)
        with self.assertRaises(TypeError):
            a.update([], {})

    def test_13_rectangle(self):
        """ Testing kwargs """
        a = Rectangle(1, 1, 1, 1, 1)
        a.update(id = 6, x=2, y=3, height =4, width=5)
        self.assertEqual(a.id, 6)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 3)
        self.assertEqual(a.width, 5)
        self.assertEqual(a.height, 4)

    def test_14_rectangle(self):
        """ Testing bad kwargs """
        a = Rectangle(1, 1, 1, 1, 1)
        a.update(hi=10, dude="bruh")
        self.assertEqual(a.__str__(), "[Rectangle] (1) 1/1 - 1/1")
    
    def test_15_rectangle(self):
        """ Testing to_dectionary """
        a = Rectangle(1, 2, 3, 4, 5)
        b = a.to_dictionary()
        self.assertEqual(type(b), dict)
        c = Rectangle(6, 6, 6, 6, 6)
        c.update(**b)
        self.assertEqual(c.__str__(), a.__str__())
