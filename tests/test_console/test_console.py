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
