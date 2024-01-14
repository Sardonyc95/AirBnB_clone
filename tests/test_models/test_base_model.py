#!/usr/bin/python3
"""Unit tests for BaseModel class."""
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    """Test cases for the BaseModel class."""

    def test_init(self):
        """Test the initialization of the BaseModel instance."""
        my_model = BaseModel()
        self.assertIsNotNone(my_model.id)
        self.assertIsNotNone(my_model.created_at)
        self.assertIsNotNone(my_model.updated_at)

    def test_str(self):
        """Test the __str__ method of the BaseModel instance."""
        my_model = BaseModel()
        str_representation = str(my_model)
        self.assertTrue("[BaseModel]" in str_representation)
        self.assertTrue(my_model.id in str_representation)

    def test_save(self):
        """Test the save method of the BaseModel instance."""
        my_model = BaseModel()
        initial_updated_at = my_model.updated_at
        my_model.save()
        self.assertNotEqual(initial_updated_at, my_model.updated_at)

    def test_to_dict(self):
        """Test the to_dict method of the BaseModel instance."""
        my_model = BaseModel()
        obj_dict = my_model.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('__class__', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('id', obj_dict)

    def test_init_with_dict(self):
        """Test initializing BaseModel instance from dictionary representation."""
        my_model = BaseModel()
        my_model.name = "My_First_Model"
        my_model.my_number = 89
        my_model_json = my_model.to_dict()

        my_new_model = BaseModel(**my_model_json)
        self.assertEqual(my_model.id, my_new_model.id)
        self.assertEqual(my_model.created_at, my_new_model.created_at)
        self.assertEqual(my_model.updated_at, my_new_model.updated_at)
        self.assertEqual(my_model.name, my_new_model.name)
        self.assertEqual(my_model.my_number, my_new_model.my_number)

        # Ensure datetime objects are of type datetime
        self.assertIsInstance(my_new_model.created_at, datetime)
        self.assertIsInstance(my_new_model.updated_at, datetime)

        # Ensure they are not the same instance
        self.assertNotEqual(my_model, my_new_model)

if __name__ == '__main__':
    unittest.main()
