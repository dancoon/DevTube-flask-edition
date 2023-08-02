"""
A module that contains the test class for the base model class.
"""
from datetime import datetime
import inspect
import mock
import models
from models.base_model import BaseModel
import pycodestyle
from time import sleep
import unittest
import uuid


module_doc = models.base_model.__doc__


class TestBaseModel(unittest.TestCase):
    """ Test for BaseModel class. """
    def setUp(self) -> None:
        """ Sets up testing environment. """
        models.storage._FileStorage__file_path = "test.json"

    def test_instatiation(self):
        """ Test for instatiation of BaseModel class. """
        b = BaseModel()
        self.assertIsInstance(b, BaseModel)
        self.assertTrue(hasattr(b, "id"))
        self.assertTrue(hasattr(b, "created_at"))
        self.assertTrue(hasattr(b, "updated_at"))
        attr = {"id": uuid.UUID,
                "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "updated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")}
        c = BaseModel(**attr)
        self.assertIsInstance(c, BaseModel)
        self.assertTrue(hasattr(c, "id"))
        self.assertTrue(hasattr(c, "created_at"))
        self.assertTrue(hasattr(c, "updated_at"))

    def test_attributes(self):
        """ Test for BaseModel class attributes. """
        b = BaseModel()
        self.assertIsInstance(b.id, str)
        self.assertIsInstance(b.created_at, datetime)
        self.assertIsInstance(b.updated_at, datetime)

    def test_str(self):
        """ Test for BaseModel class __str__ method. """
        b = BaseModel()
        self.assertEqual(str(b),
                         "[BaseModel] ({}) {}".format(b.id, b.__dict__))

    @mock.patch("models.storage")
    def test_save(self, mock_storage):
        """ Test for BaseModel class save method. """
        b = BaseModel()
        sleep(0.01)
        b.save()
        self.assertNotEqual(b.created_at, b.updated_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    def test_to_dict(self):
        """ Test for BaseModel class to_dict method. """
        b = BaseModel()
        b_dict = b.to_dict()
        self.assertIsInstance(b_dict, dict)
        self.assertIsInstance(b_dict["id"], str)
        self.assertIsInstance(b_dict["created_at"], str)
        self.assertIsInstance(b_dict["updated_at"], str)
        self.assertEqual(b_dict["__class__"], "BaseModel")

    @mock.patch("models.storage")
    def test_delete(self, mock_storage):
        """ Test for BaseModel class delete method. """
        b = BaseModel()
        b.save()
        b.delete()
        self.assertTrue(mock_storage.delete.called)


class TestBaseModelDocAndFormat(unittest.TestCase):
    """ Test BaseModel documentation and pep8. """
    def test_pep8(self):
        """ Test that models/base_model.py conforms to PEP8. """
        pep8style = pycodestyle.StyleGuide(quiet=False)
        result = pep8style.check_files(
            ["models/base_model.py", "tests/test_models/test_basemodel.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """ Test for existence of module docstring. """
        self.assertIsNot(module_doc, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(module_doc) >= 1)

    def test_class_docstring(self):
        """ Test for BaseModel class docstring. """
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1)

    def test_base_methods_docstrings(self):
        """ Test for docstrings in BaseModel methods. """
        functions = inspect.getmembers(BaseModel, inspect.isfunction)
        for name, func in functions:
            self.assertIsNot(func.__doc__, None,
                             "{:s} method needs a docstring".format(name))
            self.assertTrue(len(func.__doc__) >= 1)
