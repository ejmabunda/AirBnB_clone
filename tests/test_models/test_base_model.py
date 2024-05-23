import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid


class TestBaseModel(unittest.TestCase):
    """Unit tests for the BaseModel class."""

    def setUp(self):
        """Set up for the tests."""
        self.model = BaseModel()
        self.model.name = "My First Model"
        self.model.my_number = 89

    def test_id_is_uuid(self):
        """Test that id is a valid UUID."""
        self.assertIsInstance(self.model.id, str)
        try:
            uuid_obj = uuid.UUID(self.model.id, version=4)
        except ValueError:
            self.fail("id is not a valid UUID4 string")

    def test_created_at_is_datetime(self):
        """Test that created_at is a datetime object."""
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Test that updated_at is a datetime object."""
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """Test the string representation of the model."""
        expected_str = f"[BaseModel] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save_updates_updated_at(self):
        """Test that save() updates the updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)
        self.assertTrue(self.model.updated_at > old_updated_at)

    def test_to_dict(self):
        """Test the to_dict() method."""
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['name'], "My First Model")
        self.assertEqual(model_dict['my_number'], 89)
        self.assertEqual(model_dict['id'], self.model.id)
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
        self.assertEqual(model_dict['created_at'],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         self.model.updated_at.isoformat())

    def test_attributes_set_correctly(self):
        """Test that custom attributes are set correctly."""
        self.assertEqual(self.model.name, "My First Model")
        self.assertEqual(self.model.my_number, 89)

    def test_init_with_kwargs(self):
        """Test initializing with a dictionary."""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)
        self.assertEqual(new_model.name, self.model.name)
        self.assertEqual(new_model.my_number, self.model.my_number)


if __name__ == '__main__':
    unittest.main()
