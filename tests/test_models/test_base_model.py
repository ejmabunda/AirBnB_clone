#!/usr/bin/python3
"""This module the test class for the base model.
"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test cases for the base model.
    """
    def setUp(self):
        """Called before each test.
        """
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_init(self):
        """Test if attributes are initialized correctly.
        """
        self.assertEqual(self.model.name, "My First Model")
        self.assertEqual(self.model.my_number, 89)

    def test___str__(self):
        """Test if '__str__' returns correct representation.
        """
        expected_str = f"[{self.model.__class__.__name__}] ({self.model.id}) {self.model.__dict__}"
        # Assert that the actual string representation matches the expected format
        self.assertEqual(str(self.model), expected_str)

    def test_save(self):
        """Test if save() updates 'updated_at'.
        """
        self.model.save()
        self.assertNotEqual(self.model.created_at, self.model.updated_at)

    def test_to_dict(self):
        """Check if 'to_dict()' returns dictionary correctly.
        """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["name"], "My First Model")
        self.assertEqual(model_dict["my_number"], 89)
        self.assertIsInstance(model_dict["id"], str)
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)
        self.assertEqual(model_dict["__class__"], "BaseModel")