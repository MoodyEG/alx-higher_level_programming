#!/usr/bin/python3
from models.square import Square
import unittest
from contextlib import redirect_stdout
import io


class test_squareinit(unittest.TestCase):
    """ Testing Square class """
    def test_1_square(self):
        """ Testing if attributes are set correctly in square"""
        a = Square(20, 30, 40, 50)
        self.assertEqual(a.size, 20)
        self.assertEqual(a.x, 30)
        self.assertEqual(a.y, 40)
        self.assertEqual(a.id, 50)

    def test_2_square(self):
        """ Testing error for negative arguments """
        with self.assertRaises(ValueError):
            a = Square(-1, 1, 1)
        with self.assertRaises(ValueError):
            a = Square(1, -1, 1)
        with self.assertRaises(ValueError):
            a = Square(1, 1, -1)

    def test_3_square(self):
        """ Testing error for missing arguments """
        with self.assertRaises(TypeError):
            a = Square()

    def test_4_square(self):
        """ Testing error for too many arguments """
        with self.assertRaises(TypeError):
            a = Square(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)

    def test_4_square(self):
        """ Testing error for TypeError """
        with self.assertRaises(TypeError):
            a = Square("Hi", 1, 1)
        with self.assertRaises(TypeError):
            a = Square(1, [], 1)
        with self.assertRaises(TypeError):
            a = Square(1, 1, {})

    def test_5_square(self):
        """ Testing setter """
        a = Square(1, 1, 1)
        a.size = 20
        a.x = 30
        a.y = 40
        self.assertEqual(a.size, 20)
        self.assertEqual(a.x, 30)
        self.assertEqual(a.y, 40)

    def test_6_square(self):
        """ Testing setter type errors """
        a = Square(1, 1, 1)
        with self.assertRaises(TypeError):
            a.size = "Hi"
        with self.assertRaises(TypeError):
            a.x = {}
        with self.assertRaises(TypeError):
            a.y = ()

    def test_6_square(self):
        """ Testing setter value errors """
        a = Square(1, 1, 1)
        with self.assertRaises(ValueError):
            a.size = -1
        with self.assertRaises(ValueError):
            a.x = -1
        with self.assertRaises(ValueError):
            a.y = -1

    def test_7_square(self):
        """ Testing area """
        a = Square(20)
        self.assertEqual(a.area(), 400)

    def test_8_square(self):
        """ Testing display """
        a = Square(1, 1, 1, 1)
        expected_output = "\n #\n"
        with io.StringIO() as buf, redirect_stdout(buf):
            a.display()
            output = buf.getvalue()
        self.assertEqual(output, expected_output)

    def test_9_square(self):
        """ Testing __str__ method """
        a = Square(2, 3, 4, 5)
        self.assertEqual(a.__str__(), "[Square] (5) 3/4 - 2")

    def test_10_square(self):
        """ Testing update """
        a = Square(1, 1, 1, 1)
        a.update(89)
        self.assertEqual(a.id, 89)
        a.update(89, 3)
        self.assertEqual(a.size, 3)
        a.update(89, 3, 4)
        self.assertEqual(a.x, 4)
        a.update(89, 3, 4, 5)
        self.assertEqual(a.y, 5)

    def test_11_square(self):
        """ Testing private attributes """
        a = Square(2, 3, 4, 5)
        with self.assertRaises(AttributeError):
            print(a.__width)
        with self.assertRaises(AttributeError):
            print(a.__size)
        with self.assertRaises(AttributeError):
            print(a.__x)
        with self.assertRaises(AttributeError):
            print(a.__y)

    def test_12_square(self):
        """ Test bad args with update """
        a = Square(1, 1, 1, 1)
        with self.assertRaises(ValueError):
            a.update(1, -1)
        with self.assertRaises(TypeError):
            a.update([], {})

    def test_13_square(self):
        """ Testing kwargs """
        a = Square(1, 1, 1, 1)
        a.update(id=6, x=2, y=3, size=4)
        self.assertEqual(a.id, 6)
        self.assertEqual(a.x, 2)
        self.assertEqual(a.y, 3)
        self.assertEqual(a.size, 4)

    def test_14_square(self):
        """ Testing bad kwargs """
        a = Square(1, 1, 1, 1)
        a.update(hi=10, dude="bruh")
        self.assertEqual(a.__str__(), "[Square] (1) 1/1 - 1")

    def test_15_square(self):
        """ Testing to_dectionary """
        a = Square(2, 3, 4, 5)
        b = a.to_dictionary()
        self.assertEqual(type(b), dict)
        c = Square(6, 6, 6, 6)
        c.update(**b)
        self.assertEqual(c.__str__(), a.__str__())
