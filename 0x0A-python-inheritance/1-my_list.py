#!/usr/bin/python3
"""Main module."""


class MyList(list):
    """Class MyList inherited from list"""
    def print_sorted(self):
        """Prints the list, but sorted"""
        sl = self.copy()
        sl.sort()
        print(sl)
