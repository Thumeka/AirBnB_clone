#!/usr/bin/python3
"""Unittest for user"""
import unittest
import os
from models.user import User


class TestUser(unittest.TestCase):
    """Test case for the user class"""

    @classmethod
    def setUpClass(cls):
        """Class method to set shared resources"""
        cls.userInstance = User()
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
        """Test the public attributes in 'Place' set"""
        self.placeInstance = User()
        self.assertEqual(self.userInstance.email, "")
        self.assertEqual(self.userInstance.password, "")
        self.assertEqual(self.userInstance.first_name, "")
        self.assertEqual(self.userInstance.last_name, "")


if __name__ == "__main__":
    unittest.main()
