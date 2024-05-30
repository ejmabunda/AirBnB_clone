#!/usr/bin/python3
import unittest
from models.state import State


class TestState(unittest.TestCase):
  """Tests for the State class."""

  def test_state_initialization(self):
    """Tests that a State instance is created correctly."""
    state = State()
    self.assertIsInstance(state, State)
    self.assertEqual(state.name, "")
    self.assertIsInstance(state.id, str)
    self.assertIsInstance(state.created_at, datetime)
    self.assertIsInstance(state.updated_at, datetime)

  def test_state_with_kwargs(self):
    """Tests that a State instance can be created with keyword arguments."""
    name = "California"
    state = State(name=name)
    self.assertEqual(state.name, name)

  def test_state_str(self):
    """Tests the __str__ method of the State class."""
    state = State()
    state.name = "New York"
    expected_string = f"[State] ({state.id}) {{name: 'New York'}}"
    self.assertEqual(str(state), expected_string)


if __name__ == "__main__":
  unittest.main()
