#!/usr/bin/python3
"""Unittest for state"""
import unittest
import os
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """Test case for state class"""

    @classmethod
    def setUpClass(cls):
        """Class method to set shared resources"""
        cls.placeInstance = State()
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
        """Test public attributes of 'State' set"""
        self.stateInstance = State()
        self.assertEqual(self.stateInstance.name, "")


if __name__ == "__main__":
    unittest.main()
