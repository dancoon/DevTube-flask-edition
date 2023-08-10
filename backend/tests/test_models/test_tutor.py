"""
A module that contains the test class for the tutor class.
"""
from datetime import datetime
import inspect
import mock
import models
from models.tutor import Tutor
import pycodestyle
from time import sleep
import unittest
import uuid


module_doc = models.tutor.__doc__


class TestTutorModel(unittest.TestCase):
    """ Test for User class. """
    def setUp(self) -> None:
        """ Sets up testing environment. """
        models.storage._FileStorage__file_path = "test.json"

    def test_instatiation(self):
        """ Test for instatiation of User class. """
        t = Tutor()
        self.assertIsInstance(t, Tutor)
        self.assertTrue(hasattr(t, "id"))
        self.assertTrue(hasattr(t, "created_at"))
        self.assertTrue(hasattr(t, "updated_at"))
        self.assertTrue(hasattr(t, "name"))
        self.assertTrue(hasattr(t, "channel_name"))
        self.assertTrue(hasattr(t, "category"))
        attr = {"id": uuid.UUID,
                "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "updated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "name": "Dancoon",
                "channel_name": "Dancoon",
                "category": "Coding"}
        m = Tutor(**attr)
        self.assertIsInstance(m, Tutor)
        self.assertTrue(hasattr(m, "id"))
        self.assertTrue(hasattr(m, "created_at"))
        self.assertTrue(hasattr(m, "updated_at"))
        self.assertTrue(hasattr(m, "name"))
        self.assertTrue(hasattr(m, "channel_name"))
        self.assertTrue(hasattr(m, "category"))
        self.assertEqual(m.id, attr["id"])
        self.assertEqual(m.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                         attr["created_at"])
        self.assertEqual(m.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                         attr["updated_at"])
        self.assertEqual(m.name, attr["name"])
        self.assertEqual(m.channel_name, attr["channel_name"])
        self.assertEqual(m.category, attr["category"])

    def test_attributes(self):
        """ Test for Tutor class attributes. """
        u = Tutor()
        self.assertIsInstance(u.id, str)
        self.assertIsInstance(u.created_at, datetime)
        self.assertIsInstance(u.updated_at, datetime)
        self.assertIsInstance(u.name, str)
        self.assertIsInstance(u.channel_name, str)
        self.assertIsInstance(u.category, str)

    def test_str(self):
        """ Test for Tutor class __str__ method. """
        u = Tutor()
        self.assertEqual(str(u),
                         "[Tutor] ({}) {}".format(u.id, u.__dict__))

    @mock.patch("models.storage")
    def test_save(self, mock_storage):
        """ Test for Tutor class save method. """
        u = Tutor()
        sleep(0.01)
        u.save()
        self.assertNotEqual(u.created_at, u.updated_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    def test_to_dict(self):
        attr = {
                "name": "Dancoon",
                "channel_name": "Dancoon",
                "category": "Coding"}
        u = Tutor(**attr)
        u_dict = u.to_dict()
        self.assertIsInstance(u_dict, dict)
        self.assertIsInstance(u_dict["id"], str)
        self.assertIsInstance(u_dict["created_at"], str)
        self.assertIsInstance(u_dict["updated_at"], str)
        self.assertIsInstance(u_dict["name"], str)
        self.assertIsInstance(u_dict["channel_name"], str)
        self.assertIsInstance(u_dict["category"], str)
        self.assertEqual(u_dict["__class__"], "Tutor")

    @mock.patch("models.storage")
    def test_delete(self, mock_storage):
        """ Test for Tutor class delete method. """
        u = Tutor()
        u.save()
        u.delete()
        self.assertTrue(mock_storage.delete.called)


class TestTutorModelDocAndFormat(unittest.TestCase):
    def test_pep8_conformance_tutor(self):
        """ Test that models/tutor.py conforms to PEP8. """
        pep8style = pycodestyle.StyleGuide(quiet=False)
        result = pep8style.check_files(
            ["models/tutor.py", "tests/test_models/test_tutor.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """ Test for existence of module docstring. """
        self.assertIsNotNone(module_doc,
                             "models/tutor.py needs a docstring.")
        self.assertTrue(len(module_doc) > 1)

    def test_class_docstring(self):
        """ Test for tutor class docstring. """
        self.assertIsNotNone(Tutor.__doc__,
                             "tutor class needs a docstring.")
        self.assertTrue(len(Tutor.__doc__) >= 1)

    def test_tutor_methods_docstring(self):
        """ Test for docstrings in Tutor methods. """
        functions = inspect.getmembers(Tutor, predicate=inspect.isfunction)
        for name, func in functions:
            self.assertIsNotNone(func.__doc__,
                                 "{:s} method needs a docstring.".format(name))
            self.assertTrue(len(func.__doc__) >= 1)
