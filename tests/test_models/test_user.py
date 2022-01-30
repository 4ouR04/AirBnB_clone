#!/usr/bin/python3
<<<<<<< HEAD
"""Test User"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testuser(unittest.TestCase):
    """unit test"""
    def test_User(self):
        """
        Test Class Use
        """
        my_user = User()
        self.assertTrue(hasattr(my_user, "first_name"))
        self.assertEqual(my_user.first_name, "")
        self.assertTrue(hasattr(my_user, "last_name"))
        self.assertEqual(my_user.last_name, "")
        self.assertTrue(hasattr(my_user, "email"))
        self.assertEqual(my_user.email, "")
        self.assertTrue(hasattr(my_user, "password"))
        self.assertEqual(my_user.password, "")
=======
"""Test suite for the User class in models.user"""
import unittest
from models.base_model import BaseModel

from models.user import User


class TestUser(unittest.TestCase):
    """Test cases against the User class"""

    def test_attrs_are_class_attrs(self):
        u = User()
        # test that it is a class attribute
        self.assertTrue(hasattr(User, "first_name")
                        and hasattr(User, "last_name"))

    def test_class_attrs(self):
        u = User()
        self.assertIs(type(u.first_name), str)
        self.assertIs(type(u.last_name), str)
        self.assertTrue(u.first_name == "")
        self.assertTrue(u.last_name == "")

    def test_user_is_a_subclass_of_basemodel(self):
        u = User()
        self.assertTrue(issubclass(type(u), BaseModel))
>>>>>>> ab680e0da1b3fa8090fb95252d6db9d0c0e4ae7f
