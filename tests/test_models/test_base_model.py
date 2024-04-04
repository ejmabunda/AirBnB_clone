#!/usr/bin/python3
"""This module suppiles the test class for the base model."""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Test class for the base model."""
    def setUp(self):
        """Called before each test."""
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def tearDown(self):
        """Called after each test."""
        pass

    def test_attributes(self):
        self.assertEqual(self.my_model.name, "My First Model")
        self.assertEqual(self.my_model.my_number, 89)

    def test_save(self):
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        self.assertNotEqual(self.my_model.updated_at, old_updated_at)

    def test_to_dict(self):
        model_json = self.my_model.to_dict()
        self.assertEqual(model_json["my_number"], 89)
        self.assertEqual(model_json["name"], "My First Model")
        self.assertEqual(model_json["__class__"], "BaseModel")
        self.assertEqual(model_json["id"], self.my_model.id)
        self.assertTrue(isinstance(model_json["created_at"], str))
        self.assertTrue(isinstance(model_json["updated_at"], str))
