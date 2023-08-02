"""
A module that contains the test class for the user class.
"""
from datetime import datetime
import inspect
import mock
import models
from models.user import User
import pycodestyle
from time import sleep
import unittest
import uuid


module_doc = models.user.__doc__


class TestUserModel(unittest.TestCase):
    """ Test for User class. """
    def setUp(self) -> None:
        """ Sets up testing environment. """
        models.storage._FileStorage__file_path = "test.json"

    def test_instatiation(self):
        """ Test for instatiation of User class. """
        u = User()
        self.assertIsInstance(u, User)
        self.assertTrue(hasattr(u, "id"))
        self.assertTrue(hasattr(u, "created_at"))
        self.assertTrue(hasattr(u, "updated_at"))
        self.assertTrue(hasattr(u, "email"))
        self.assertTrue(hasattr(u, "password"))
        self.assertTrue(hasattr(u, "first_name"))
        self.assertTrue(hasattr(u, "last_name"))
        attr = {"id": uuid.UUID,
                "created_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "updated_at": datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f"),
                "email": "test@gmail.com",
                "password": "test_pwd",
                "first_name": "Joe",
                "last_name": "Doe"}
        m = User(**attr)
        self.assertIsInstance(m, User)
        self.assertTrue(hasattr(m, "id"))
        self.assertTrue(hasattr(m, "created_at"))
        self.assertTrue(hasattr(m, "updated_at"))
        self.assertTrue(hasattr(m, "email"))
        self.assertTrue(hasattr(m, "password"))
        self.assertTrue(hasattr(m, "first_name"))
        self.assertTrue(hasattr(m, "last_name"))
        self.assertEqual(m.id, attr["id"])
        self.assertEqual(m.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                         attr["created_at"])
        self.assertEqual(m.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                         attr["updated_at"])
        self.assertEqual(m.email, attr["email"])
        self.assertEqual(m.password, attr["password"])
        self.assertEqual(m.first_name, attr["first_name"])
        self.assertEqual(m.last_name, attr["last_name"])

    def test_attributes(self):
        """ Test for User class attributes. """
        u = User()
        self.assertIsInstance(u.id, str)
        self.assertIsInstance(u.created_at, datetime)
        self.assertIsInstance(u.updated_at, datetime)
        self.assertIsInstance(u.email, str)
        self.assertIsInstance(u.password, str)
        self.assertIsInstance(u.first_name, str)
        self.assertIsInstance(u.last_name, str)

    def test_str(self):
        """ Test for User class __str__ method. """
        u = User()
        self.assertEqual(str(u),
                         "[User] ({}) {}".format(u.id, u.__dict__))

    @mock.patch("models.storage")
    def test_save(self, mock_storage):
        """ Test for User class save method. """
        u = User()
        self.assertEqual(u.created_at, u.updated_at)
        sleep(0.01)
        u.save()
        self.assertNotEqual(u.created_at, u.updated_at)
        self.assertTrue(mock_storage.new.called)
        self.assertTrue(mock_storage.save.called)

    def test_to_dict(self):
        attr = {
                "email": "test@gmail.com",
                "password": "test_pwd",
                "first_name": "Joe",
                "last_name": "Doe"}
        u = User(**attr)
        u_dict = u.to_dict()
        self.assertIsInstance(u_dict, dict)
        self.assertIsInstance(u_dict["id"], str)
        self.assertIsInstance(u_dict["created_at"], str)
        self.assertIsInstance(u_dict["updated_at"], str)
        self.assertIsInstance(u_dict["email"], str)
        self.assertIsInstance(u_dict["password"], str)
        self.assertIsInstance(u_dict["first_name"], str)
        self.assertIsInstance(u_dict["last_name"], str)
        self.assertEqual(u_dict["__class__"], "User")

    @mock.patch("models.storage")
    def test_delete(self, mock_storage):
        """ Test for User class delete method. """
        u = User()
        u.save()
        u.delete()
        self.assertTrue(mock_storage.delete.called)


class TestUserModelDocAndFormat(unittest.TestCase):
    def test_pep8_conformance_user(self):
        """ Test that models/user.py conforms to PEP8. """
        pep8style = pycodestyle.StyleGuide(quiet=False)
        result = pep8style.check_files(
            ["models/user.py", "tests/test_models/test_user.py"])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstring(self):
        """ Test for existence of module docstring. """
        self.assertIsNotNone(module_doc,
                             "models/user.py needs a docstring.")
        self.assertTrue(len(module_doc) > 1)

    def test_class_docstring(self):
        """ Test for User class docstring. """
        self.assertIsNotNone(User.__doc__,
                             "User class needs a docstring.")
        self.assertTrue(len(User.__doc__) >= 1)

    def test_user_methods_docstring(self):
        """ Test for docstrings in User methods. """
        functions = inspect.getmembers(User, predicate=inspect.isfunction)
        for name, func in functions:
            self.assertIsNotNone(func.__doc__,
                                 "{:s} method needs a docstring.".format(name))
            self.assertTrue(len(func.__doc__) >= 1)
