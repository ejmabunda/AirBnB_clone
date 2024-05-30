#!/usr/bin/python3
import unittest
from models.state import State

class TestState(unittest.TestCase):
    def test_default_name(self):
        # Create an instance of State with default name
        state = State()
        self.assertEqual(state.name, "")

    def test_custom_name(self):
        # Create an instance of State with a custom name
        custom_name = "California"
        state = State(name=custom_name)
        self.assertEqual(state.name, custom_name)

    def test_name_assignment(self):
        # Assign a new name to an existing State instance
        state = State()
        new_name = "New York"
        state.name = new_name
        self.assertEqual(state.name, new_name)

    def test_name_type(self):
        # Ensure that the name attribute is of type str
        state = State()
        self.assertIsInstance(state.name, str)

if __name__ == "__main__":
    unittest.main()
