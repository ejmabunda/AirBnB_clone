import unittest
from models.city import City

class TestCity(unittest.TestCase):
    def test_default_state_id(self):
        # Create an instance of City with default state_id
        city = City()
        self.assertEqual(city.state_id, "")

    def test_custom_state_id(self):
        # Create an instance of City with a custom state_id
        custom_state_id = "CA"
        city = City(state_id=custom_state_id)
        self.assertEqual(city.state_id, custom_state_id)

    def test_default_name(self):
        # Create an instance of City with default name
        city = City()
        self.assertEqual(city.name, "")

    def test_custom_name(self):
        # Create an instance of City with a custom name
        custom_name = "Los Angeles"
        city = City(name=custom_name)
        self.assertEqual(city.name, custom_name)

    def test_name_assignment(self):
        # Assign a new name to an existing City instance
        city = City()
        new_name = "San Francisco"
        city.name = new_name
        self.assertEqual(city.name, new_name)

    def test_name_type(self):
        # Ensure that the name attribute is of type str
        city = City()
        self.assertIsInstance(city.name, str)

if __name__ == "__main__":
    unittest.main()
