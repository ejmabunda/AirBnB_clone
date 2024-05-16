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
        expected_str = (f"[{self.model.__class__.__name__}] "
                        f"({self.model.id}) {self.model.__dict__}")
        # Assert that the actual string representation matches
        # # the expected format
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

    # Test for id uniqueness
    def test_id_uniqueness(self):
        """Tests if different instances have unique IDs."""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    # Test to_dict output format
    def test_to_dict_format(self):
        """Tests if to_dict returns a dictionary with expected keys."""
        model_dict = self.model.to_dict()
        expected_keys = {"id",
                         "created_at",
                         "updated_at",
                         "__class__",
                         "name",
                         "my_number"}
        self.assertEqual(set(model_dict.keys()), expected_keys)

    # Test if to_dict converts datetime to string
    def test_to_dict_datetime(self):
        """Tests if to_dict converts datetime attributes to strings."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict["created_at"], str)
        self.assertIsInstance(model_dict["updated_at"], str)

    # Test if new model from dict has same attributes
    def test_new_model_from_dict(self):
        """Tests if creating a new model from dict
        creates an equal instance."""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(self.model.id, new_model.id)
        self.assertEqual(self.model.name, new_model.name)
        self.assertEqual(self.model.my_number, new_model.my_number)
        # Assert timestamps are equal but may differ
        # slightly due to microseconds
        self.assertEqual(self.model.created_at, new_model.created_at)
        self.assertEqual(self.model.updated_at, new_model.updated_at)

    # Test that new model from dict is a different object
    def test_new_model_from_dict_different_object(self):
        """Tests if creating a new model from dict creates
        a different object."""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertIsNot(self.model, new_model)
