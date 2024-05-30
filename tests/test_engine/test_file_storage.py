#!/usr/bin/python3
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from datetime import datetime
import os


class TestFileStorage(unittest.TestCase):
    """Unit tests for the FileStorage class."""

    def setUp(self):
        """Set up for the tests."""
        self.storage = FileStorage()

    def tearDown(self):
        """Clean up after each test."""
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_all(self):
        """Test the all() method."""
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        """Test the new() method."""
        model = BaseModel()
        self.storage.new(model)
        key = "{}.{}".format(model.__class__.__name__, model.id)
        self.assertIn(key, self.storage.all())

    def test_save_and_reload(self):
        """Test the save() and reload() methods."""
        model = BaseModel()
        model.name = "Test Model"
        model.save()

        # Check if the file exists after saving
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

        # Reload the data and check if the reloaded object is correct
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        self.assertIn("BaseModel.{}".format(model.id), objects)

        reloaded_model = objects["BaseModel.{}".format(model.id)]
        self.assertIsInstance(reloaded_model, BaseModel)
        self.assertEqual(reloaded_model.id, model.id)
        self.assertEqual(reloaded_model.name, "Test Model")
        self.assertIsInstance(reloaded_model.created_at, datetime)
        self.assertIsInstance(reloaded_model.updated_at, datetime)
