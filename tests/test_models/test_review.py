#!/usr/bin/python3
"""Test Review"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models.user import User


class Testreview(unittest.TestCase):
    """unit test"""
    def test_class(self):
        rev1 = Review()
        self.assertEqual(rev1.__class__.__name__, "Review")

    def test_father(self):
        rev1 = Review()
        self.assertTrue(issubclass(rev1.__class__, BaseModel))

    def test_review(self):
        """
        Test review
        """
        my_review = Review()
        self.assertTrue(hasattr(my_review, "place_id"))
        self.assertEqual(my_review.place_id, "")
        self.assertTrue(hasattr(my_review, "user_id"))
        self.assertEqual(my_review.user_id, "")
        self.assertTrue(hasattr(my_review, "text"))
        self.assertEqual(my_review.text, "")
