#!/usr/bin/python3
""" Test module for consol.py """
import unittest
from unittest.mock import patch
from io import StringIO
from models import storage
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
""" Test class of hbnb """

    @patch('sys.stdout', new_callable=StringIO)
    def assert_stdout(self, expected_output, func, *args, **kwargs):
        with self.subTest():
            func(*args, **kwargs)
            self.assertEqual(sys.stdout.getvalue().strip(), expected_output)

    def setUp(self):
        self.cmd = HBNBCommand()

    def test_do_quit(self):
        self.assertTrue(self.cmd.do_quit(None))

    def test_do_EOF(self):
        with patch('builtins.input', return_value='EOF'):
            self.assertTrue(self.cmd.do_EOF(None))

    def test_emptyline(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.emptyline()
            self.assertEqual(mock_stdout.getvalue(), '')

    def test_do_create(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.cmd.do_create("BaseModel")
            self.assertTrue(mock_stdout.getvalue().strip())

    def test_do_show(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Assuming you have a valid object_id for the class in your storage
            self.cmd.do_show("BaseModel 123")
            self.assertTrue(mock_stdout.getvalue().strip())

    def test_do_destroy(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            # Assuming you have a valid object_id for the class in your storage
            self.cmd.do_destroy("BaseModel 123")
            self.assertTrue(mock_stdout.getvalue().strip())


if __name__ == '__main__':
    unittest.main()
