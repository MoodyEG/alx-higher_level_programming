#!/usr/bin/python3
""" Base Test module """
from models.base import Base
import unittest



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
