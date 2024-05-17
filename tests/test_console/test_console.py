import unittest
from console import HBNBCommand

class TestConsole(unittest.TestCase):

    def setUp(self):
        self.hbnb = HBNBCommand()

    def test_quit(self):
        """Test quit command"""
        self.assertTrue(self.hbnb.onecmd("quit"))

    def test_EOF(self):
        """Test EOF command"""
        self.assertTrue(self.hbnb.onecmd("EOF"))

    def test_emptyline(self):
        """Test empty line command"""
        self.assertIsNone(self.hbnb.emptyline())

    def test_emptyline_with_spaces(self):
        """Test empty line with spaces command"""
        self.assertIsNone(self.hbnb.onecmd("   "))

    def test_precmd(self):
        """Test precmd method"""
        self.assertEqual(self.hbnb.precmd("   test   "), "test")
