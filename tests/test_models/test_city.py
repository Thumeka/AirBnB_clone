#!/usr/bin/python3
"""Unittest for city class"""
import unittest
import os
from models.city import City


class TestCity(unittest.TestCase):
    """Test case for the city class"""

    @classmethod
    def setUpClass(cls):
        """Class method to set shared resources"""
        cls.cityInstance = City()
        try:
            os.rename("file.json", "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close test environment"""
        try:
            os.remove("file.json")
            os.rename("test_file.json", "file.json")
        except Exception:
            pass

    def test_attributes(self):
        """Test case for class attributes"""
        self.assertEqual(self.cityInstance.state_id, "")
        self.assertEqual(self.cityInstance.name, "")


if __name__ == "__main__":
    unittest.main()
