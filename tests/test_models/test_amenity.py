#!/usr/bin/python3
"""Test module for amenity"""

import unittest

from models import amenity

class Test_amenity(unittest.Testcase):


    def test_amenity_in_dict(self):
        self.AssertTrue('id' in self.Amenity__dict__)


    if __main__ == '__name__':
        unittest.main()
