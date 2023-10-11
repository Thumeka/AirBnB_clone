#!/usr/bin/python3
"""Module for testing Base Model Class"""

import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Suite of Base Model tests"""
    model = BaseModel()

    def test_init(self):
        """Test the initialization of the BaseModel"""
        self.assertIsInstance(self.model.id, str)
        self.assertIsInstance(self.model.created_at, datetime)
        self.assertIsInstance(self.model.updated_at, datetime)

        model2 = BaseModel()
        self.assertNotEqual(self.model.id, model2.id)

    def test_str(self):
        """Test the string representation of BaseModel instance"""
        model_str = str(self.model)
        self.assertIn("BaseModel", model_str)
        self.assertIn(self.model.id, model_str)
        self.assertIn(str(self.model.__dict__), model_str)

    def test_save(self):
        """Test the 'save' method of BaseModel"""
        og_updated = self.model.updated_at
        self.model.save()
        new_updated = self.model.updated_at
        self.assertNotEqual(og_updated, new_updated)

    def test_to_dict(self):
        "Test the 'to_dict' method of BaseModel"
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertAlmostEqual(
            model_dict['updated_at'], self.model.created_at.isoformat())


if __name__ == 'main':
    unittest.main()
