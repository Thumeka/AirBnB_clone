#!/usr/bin/python3
"""Unittest for review class"""
import unittest
import os
from models.review import Review


class TestReview(unittest.TestCase):
    """Test case for the Review class"""

    @classmethod
    def setUpClass(cls):
        """Class method to set shared resources"""
        cls.reviewInstance = Review()
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
        """Test the public attributes"""
        self.assertEqual(self.reviewInstance.place_id, "")
        self.assertEqual(self.reviewInstance.user_id, "")
        self.assertEqual(self.reviewInstance.text, "")


if __name__ == "__main__":
    unittest.main()
