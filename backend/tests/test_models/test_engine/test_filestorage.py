"""
A module that contains the test class for the file storage class.
"""
import unittest
from models.engine.filestorage import FileStorage
from models.base_model import BaseModel
import pycodestyle
import models
import inspect

module_doc = FileStorage.__doc__


class TestFileStorage(unittest.TestCase):
    """ Test for FileStorage class. """
    def setUp(self) -> None:
        """ Sets up testing environment. """
        FileStorage._FileStorage__objects = {}
        models.storage._FileStorage__file_path = "test.json"
        self.filestorage = FileStorage()

    def test_all(self):
        """ Test for all method. """
        returned_item = FileStorage().all()
        self.assertIsInstance(returned_item, dict)
        self.assertIs(returned_item, FileStorage._FileStorage__objects)

    def test_new(self):
        """ Test for new method. """
        objects = FileStorage._FileStorage__objects
        self.assertEqual(len(objects), 0)
        b = BaseModel()
        self.filestorage.new(b)
        self.assertEqual(len(objects), 1)

    def test_save(self):
        """ Test for save method. """
        pass


class TestFileStorageDocAndFormat(unittest.TestCase):
    """ Test for documentation and pep8. """
    def test_pep8_conformance_filestorage(self):
        """ Test that we conform to PEP8. """
        pep8style = pycodestyle.StyleGuide(quiet=False)
        result = pep8style.check_files(
            ["models/engine/filestorage.py",
             "tests/test_models/test_engine/test_filestorage.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """ Test for existence of module docstring. """
        self.assertIsNotNone(module_doc,
                             "filestorage.py needs a docstring.")
        self.assertTrue(len(module_doc) > 1)

    def test_class_docstring(self):
        """ Test for FileStorage class docstring. """
        self.assertIsNotNone(FileStorage.__doc__,
                             "FileStorage class needs a docstring.")
        self.assertTrue(len(FileStorage.__doc__) >= 1)

    def test_filestorage_methods_docstrings(self):
        functions = inspect.getmembers(FileStorage, inspect.isfunction)
        for name, func in functions:
            self.assertIsNotNone(func.__doc__,
                                 "{:s} method needs a docstring.".format(name))
            self.assertTrue(len(func.__doc__) >= 1)
