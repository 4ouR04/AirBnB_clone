#!/usr/bin/python3
<<<<<<< HEAD
"""Amenity"""
import unittest
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.state import State
from models.review import Review


class Testamenity(unittest.TestCase):
    """unit test"""
    def test_class(self):
        amen = Amenity()
        self.assertEqual(amen.__class__.__name__, "Amenity")

    def test_base(self):
        amen = Amenity()
        self.assertTrue(issubclass(amen.__class__, BaseModel))

    def test_amenity(self):
        """Test attributes of Class Amenity"""
        amenity = Amenity()
        self.Assert true(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_dict_value(self):
        """
            test dict values
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        inst = Amenity()
        dict_con = inst.to_dict()
        self.assertEqual(dict_con["__class__"], "Amenity")
        self.assertEqual(type(dict_con["created_at"]), str)
        self.assertEqual(type(dict_con["updated_at"]), str)
        self.assertEqual(
                            dict_con["created_at"],
                            inst.created_at.strftime(time_format)
                                        )
        self.assertEqual(
                            dict_con["updated_at"],
                            inst.updated_at.strftime(time_format))
=======
"""Test suite for Amenity class of the models.amenity module"""
import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        self.amenity = Amenity()

    def test_amenity_is_a_subclass_of_basemodel(self):
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attr_is_a_class_attr(self):
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attr(self):
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(getattr(self.amenity, "name")))
>>>>>>> ab680e0da1b3fa8090fb95252d6db9d0c0e4ae7f
