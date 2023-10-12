#!/usr/bin/python3
"""Unittest for amenity"""
import unittest
import os
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test case for amenity class"""

    @classmethod
    def setUpClass(cls):
        """Class method to set shared resources"""
        cls.amenityInstance = Amenity()
        try:
            os.rename("file.json", "test_file.json")
        except FileNotFoundError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close shared resources"""
        try:
            os.rename("test_file.json", "file.json")
        except FileNotFoundError:
            pass

    def test_attributes(self):
        """Test for the public atrributes of "Amenity" set"""
        self.amenityInstance = Amenity()
        self.assertEqual(self.amenityInstance.name, "")


if __name__ == "__main__":
    unittest.main()
