#!/usr/bin/python3
"""Unittest for place class"""
import unittest
import os
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test case for place class"""

    @classmethod
    def setUpClass(cls):
        """Class method to set shared resources"""
        cls.placeInstance = Place()
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
        """Test public attributes of 'Place' set"""
        self.assertEqual(self.placeInstance.city_id, "")
        self.assertEqual(self.placeInstance.user_id, "")
        self.assertEqual(self.placeInstance.name, "")
        self.assertEqual(self.placeInstance.description, "")
        self.assertEqual(self.placeInstance.number_rooms, 0)
        self.assertEqual(self.placeInstance.number_bathrooms, 0)
        self.assertEqual(self.placeInstance.max_guest, 0)
        self.assertEqual(self.placeInstance.price_by_night, 0)
        self.assertEqual(self.placeInstance.latitude, 0.0)
        self.assertEqual(self.placeInstance.longitude, 0.0)
        self.assertEqual(self.placeInstance.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
