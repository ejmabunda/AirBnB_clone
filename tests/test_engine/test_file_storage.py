#!/usr/bin/python3
"""This module tests the FileStorage class."""
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
import os


class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class.
    """
    def setUp(self):
        """Called before each test.
        """
        self.storage = FileStorage()
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89
        self.storage.new(self.model)
        self.storage.save()

    def tearDown(self):
        """Called after each test.
        """
        #self.storage.delete(self.model)
        del self.model
        # Remove any created JSON file
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        """Test if FileStorage.all returns the object dictionary.
        """
        self.storage.new(self.model)
        self.assertIs(self.storage.all(), self.storage.all())

    def test_new(self):
        """Test if FileStorage.new adds object to internal dict.
        """
        key = f"{self.model.__class__.__name__}.{self.model.id}"
        self.storage.new(self.model)
        self.assertIn(key, self.storage.all())

    def test_save(self):
        """Test if FileStorage.save writes objects to JSON.
        """
        self.storage.new(self.model)
        self.storage.save()
        # Check if file exists (doesn't directly test functionality)
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_existing_file(self):
        """Test if FileStorage.reload loads objects from JSON.
        """