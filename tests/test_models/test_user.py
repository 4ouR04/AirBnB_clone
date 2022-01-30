#!/usr/bin/python3
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
