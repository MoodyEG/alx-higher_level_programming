#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Tests for max_integer function """

    def test_1_max(self):
        """ Max at the end """
        self.assertEqual(max_integer([2, 9, 5, 55]), 55)

    def test_2_max(self):
        """ Max at the beginning """
        self.assertEqual(max_integer([200, 9, 5, 55]), 200)

    def test_3_max(self):
        """ Max in the middle """
        self.assertEqual(max_integer([2, 9, 100, 5, 55]), 100)

    def test_4_max(self):
        """ Testing negative """
        self.assertEqual(max_integer([2, 9, -5, 55]), 55)
        self.assertEqual(max_integer([-2, -9, -5, -55]), -2)

    def test_5_max(self):
        """ Testing 1 element """
        self.assertEqual(max_integer([2]), 2)

    def test_6_max(self):
        """ Empty list """
        self.assertEqual(max_integer([2]), None)
