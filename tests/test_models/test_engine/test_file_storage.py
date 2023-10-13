#!/usr/bin/python3
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Test case for the 'FileStorage' class"""

    @classmethod
    def setUpClass(cls):
        """Class method to set shared resources"""
        cls.storage = FileStorage()
        try:
            os.rename(FileStorage._FileStorage__file_path, "test_file.json")
        except Exception:
            pass

    @classmethod
    def tearDownClass(cls):
        """Class method to close shared resources"""
        try:
            os.remove(FileStorage._FileStorage__file_path)
            os.rename("test_file.json", FileStorage._FileStorage__file_path)
        except Exception:
            pass

    def test_all(self):
        """Test case for 'all' method"""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test case for 'new' method"""
        mode = BaseModel()
        self.storage.new(mode)
        key = mode.__class__.__name__ + "." + mode.id
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test case for 'save' method"""
        mode = BaseModel()
        self.storage.new(mode)
        self.storage.save()
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        """Test case for 'reload' method"""
        mode = BaseModel()
        self.storage.new(mode)
        self.storage.save()
        self.storage._FileStorage__objects.clear()
        self.storage.reload()
        key = mode.__class__.__name__ + "." + mode.id
        self.assertIn(key, self.storage.all())


if __name__ == "__main__":
    unittest.main()
